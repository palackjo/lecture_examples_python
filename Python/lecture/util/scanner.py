import re

class TokenType():
	bracket_open = 1
	bracket_close = 2
	variable = 3
	value = 4
	operator = 5
	whitespace = 6
	function = 7


class Scanner():

	def __init__(self, operator_list, open_bracket, close_bracket, function_list):
		self.operator_list = operator_list
		self.open_bracket = open_bracket
		self.close_bracket = close_bracket
		self.function_list = function_list

	def scan(self, term):
		tokens = []

		while 1:			
			char = term[:1]
			term = term[1:]
			temp = ''

			if self.is_whitespace(char):
				tokens.append((char, TokenType.whitespace))

			elif self.is_opening_bracket(char):
				tokens.append((char, TokenType.bracket_open))
			
			elif self.is_closing_bracket(char):
				tokens.append((char, TokenType.bracket_close))

			elif self.is_operator_char(char):
				temp = temp + char
				while 1:
					char = term[:1]
					if not self.is_operator_char(char, temp=temp):
						break	
					term = term[1:]				
					temp = temp + char
					if len(term) == 0:
						break

				if not self.is_operator(temp):
					raise Exception('Cannot parse operator "%s"' % temp)
				tokens.append((temp, TokenType.operator))

			elif self.is_variable_start(char):
				temp = temp + char
				while 1:
					char = term[:1]
					if not self.is_variable_char(char):
						break						
					term = term[1:]		
					temp = temp + char
					if len(term) == 0:
						break

				# check if the parsed string is expected to be a function
				if self.is_function(temp):
					tokens.append((temp, TokenType.function))
				else:
					tokens.append((temp, TokenType.variable))

			elif self.is_value(char):
				temp = temp + char
				while 1:
					char = term[:1]
					if not self.is_value(char, temp=temp):
						break						
					term = term[1:]		
					temp = temp + char
					if len(term) == 0:
						break
				tokens.append((temp, TokenType.value))

			else:
				raise Exception('Cannot parse token "%s"' % char)

			if len(term) == 0:
				break

		return tokens

	def is_value(self, char, temp=''):
		p = re.compile('^[0-9\.]+$')
		if p.match(temp + char):
			return True
		return False

	def is_operator(self, operator):
		for o in self.operator_list:
			if o == operator:
				return True

		return False

	def is_function(self, function):
		for f in self.function_list:
			if f == function:
				return True

		return False

	def is_operator_char(self, char, temp=''):
		for operator in self.operator_list:
			if (temp == operator[len(temp):] or temp == '') and str(temp + char) == operator[:len(temp) + 1]:
				return True
		return False

	def is_variable_start(self, char):
		p = re.compile('[a-zA-Z]')
		if p.match(char):
			return True
		return False

	def is_variable_char(self, char):
		p = re.compile('[a-zA-Z0-9_]')
		if p.match(char):
			return True
		return False

	def is_opening_bracket(self, char):
		if self.open_bracket == char:
			return True
		return False

	def is_closing_bracket(self, char):
		if self.close_bracket == char:
			return True
		return False

	def is_whitespace(self, char):
		p = re.compile('[\s]')
		if p.match(char):
			return True
		return False

if __name__ == '__main__':
	operator_list = ['+', '-', '*', '/', '**']
	function_list = ['sin']
	open_bracket = '('
	close_bracket = ')'
	scanner = Scanner(operator_list, open_bracket, close_bracket, function_list)
	tokens = scanner.scan('(1+2+3+4)+sin(5)+(6+767+4)*1*2/3434*varr0c0')

	print(tokens)
	assert tokens == ['(', '1', '+', '2', '+', '3', '+', '4', ')', '+', 'sin', '(', '5', ')', '+', '(', '6', '+', '767', '+', '4', ')', '*', '1', '*', '2', '/', '3434', '*', 'a123']