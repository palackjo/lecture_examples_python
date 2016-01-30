# diff.stlx translation

from lecture.util import Scanner, TokenType

# differentiate expr_list by x
def diff(expr, x):
    value, tokentype = expr[0]
    # operations on first element if exist
    if len(expr) == 1:
        if tokentype == TokenType.variable:
            if value == x:
                return 1
            else:
                return 0

        if tokentype == TokenType.value:
            return 0

    if tokentype == TokenType.operator and value == '-':
        return ['-', ]

def test_diff(expr):
    operator_list  = ['+', '-', '*', '/', '**']
    function_list  = ['sin']
    open_bracket   = '('
    close_bracket  = ')'
    scanner        = Scanner(operator_list, open_bracket, 
                            close_bracket, function_list)
    tokens         = scanner.scan(expr)

    # remove whitespaces
    cleaned_tokens = [token for token in tokens 
                      if not token[1] == TokenType.whitespace]
