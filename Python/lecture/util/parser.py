if __name__ == '__main__':
    from scanner import Scanner, TokenType
    from helper import is_number
else:
    from .scanner import Scanner, TokenType
    from .helper import is_number


class MatchParser():

    def __init__(self, test=False):
        self.test = test
        operator_list = ['+', '-', '*', '/', '%', '**', '&&', '||', '<', '<=', '=>', '<==>', '>', '>=', '==', '!=', '!']
        function_list = ['sin', 'log', 'exp', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'ln']
        open_bracket = '('
        close_bracket = ')'

        self.scanner = Scanner(operator_list, open_bracket, close_bracket, function_list)
        self.token_stack = []
        self.argument_stack = []
        self.operator_stack = []

    def pop_and_evaluate(self):
        (value, tokentype) = self.operator_stack.pop()
        result = ''
        if self.is_unary_operator((value, tokentype)):
            argument = self.argument_stack.pop()

            if tokentype == TokenType.function:
                result = "%s(%s)" % (value, argument)
            elif tokentype == TokenType.operator and value == '!':
                result = "!%s" % (argument,)

        else:
            rhs = self.argument_stack.pop()
            lhs = self.argument_stack.pop()
            result = "%s %s %s" % (rhs, value, lhs)

        self.argument_stack.append(result)

    def eval_before(self, stack_operator, next_operator):
        (stack_value, stack_tokentype) = stack_operator
        (next_value, next_tokentype) = next_operator

        if stack_tokentype == TokenType.bracket_open:
            return False

        if self.precedence((stack_value, stack_tokentype)) > self.precedence((next_value, next_tokentype)):
            return True
        elif self.is_unary_operator((stack_value, stack_tokentype)) \
                and self.is_unary_operator((next_value, next_tokentype)):
            return False
        elif self.precedence((stack_value, stack_tokentype)) == self.precedence((next_value, next_tokentype)):
            if stack_value == next_value:
                return self.is_left_associative((stack_value, stack_tokentype))
            return True
        return False

    def precedence(self, token):
        (value, tokentype) = token
        if self.is_unary_operator(token):
            return 6
        if tokentype == TokenType.operator:
            if value in ['**']:
                return 5
            if value in ['*', '/', '%']:
                return 4
            if value in ['+', '-']:
                return 3
            if value in ['>', '<', '<=', '=>', '<==>', '>=', '==', '!=']:
                return 2
            if value in ['&&']:
                return 1
            if value in ['||']:
                return 0
        raise Exception('unknown operator at precedence %s' % value)

    def is_left_associative(self, token):
        (value, tokentype) = token
        if value in ['+', '-', '*', '/', '%', '||', '&&', '<=', '==', '<', '>', '>=', '=>', '<==>', '!=']:
            return True
        if value in ['**']:
            return False
        if self.is_unary_operator(token):
            return False
        raise Exception('unknown operator at is left associative %s' % value)

    def is_unary_operator(self, token):
        (value, tokentype) = token
        if tokentype == TokenType.function \
                or tokentype == TokenType.operator and value == '!':
            return True
        return False

    def parse(self, input):
        self.token_stack = self.scanner.scan(input)
        self.token_stack = [x for x in self.token_stack if not x[1] == TokenType.whitespace]
        self.token_stack.reverse()

        while self.token_stack:
            (value, tokentype) = self.token_stack.pop()
            if tokentype in [TokenType.value, TokenType.variable]:
                self.argument_stack.append(value)
                continue

            if not self.operator_stack or tokentype == TokenType.bracket_open:
                self.operator_stack.append((value, tokentype))
                continue

            (operator_value, operator_tokentype) = self.operator_stack[-1]

            if operator_tokentype == TokenType.bracket_open and \
                            tokentype == TokenType.bracket_close:
                self.operator_stack.pop()

            elif tokentype == TokenType.bracket_close \
                    or self.eval_before((operator_value, operator_tokentype), (value, tokentype)):
                self.pop_and_evaluate()
                self.token_stack.append((value, tokentype))

            else:
                self.operator_stack.append((value, tokentype))

        while len(self.operator_stack) - 1 > 0:
            self.pop_and_evaluate()

        if len(self.operator_stack) > 0:
            result = (self.operator_stack[0], self.argument_stack)
        elif len(self.argument_stack) > 0:
            result = self.argument_stack

        self.operator_stack = []
        self.argument_stack = []
        return result

    def match(self, scheme, value):
        try:
            result_scheme = self.parse(scheme)
            result_value = self.parse(value)

            if len(result_scheme) < 2 or len(result_value) < 2:
                if len(result_scheme) == 1 and len(result_value) == 1:
                    if is_number(result_scheme[0]) == is_number(result_value[0]):
                        self.values = {}
                        self.values[result_scheme[0]] = result_value[0]
                        return True
                return False

            (scheme_operator, scheme_values) = result_scheme
            (value_operator, value_values) = result_value

            (value_operator_value, value_operator_tokentype) = value_operator
            (scheme_operator_value, scheme_operator_tokentype) = scheme_operator

            if value_operator_value == scheme_operator_value:
                self.values = {}
                for idx, x in enumerate(scheme_values):
                    self.values[x] = value_values[idx]
                if self.test:
                    print(self.values)
                return True
            return False
        except:
            pass

    def is_number(self, value):
        return self.match('1', value)

    def is_variable(self, value):
        return self.match('a', value)



if __name__ == '__main__':
    parser = MatchParser()
    result = parser.match("p||q", "2**4==10000000||123==!True")
    print(parser.values["p"])
    print(parser.values["q"])
    assert result is True
    result = parser.match("p==q", "2**4==10000000||123==!True")
    assert result is False
    result = parser.match("sin(a)", "sin(2**3||2**5)")
    print(parser.values["a"])
    assert result is True
    result = parser.match("!l", "varr0c0")
    assert result is False
    result = parser.match("l", "varr0c0")
    assert result is True
