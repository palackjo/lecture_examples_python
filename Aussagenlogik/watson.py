def evaluate(f, i):
	match(f, cases=[
		["True", True],
		["False", False],
		[match.is_var("p"), i[p]],
		["!g", !evaluate(g, i)]],
		["g && h", evaluate(g, i) && evaluate(h,i)],
		["g || h", evaluate(g, i) || evaluate(h, i)],
		["g => h", not(evaluate(g, i)) or evaluate(h,i)],
		["g <==> h", evaluate(g,i) == evaluate(h,i)],
		["default", raise SyntaxError('Syntax error in evaluate(%s, %s)' % (f, i))])

# This procedure turns a subset m of the list of all variables
# into a propositional valuation that's result is True if
# x is an element of m.
def create_valuation(m, v):
	{x: x in m for x in v}

# Austin, Brian or Colin is guilty (logical or).
f1 = 'a || b || c'
# If Austin is guilty, he has exactly one accomplice.
f2 = 'a => b || c' 		# at least one accomplice
f3 = 'a => !(b && c)' 	# at most one accomplice
# If Brian is innocent, then Colin is innocent too.
f4 = '!b => !c'
# If exactly two are guilty, then Colin is one of them.
f5 = '!(a && b && !c)'
# If Colin is innocent, then Austin is guilty.
f6 = '!c => a'

fs = [f1, f2, f3, f4, f5, f6]
v = Set('a', 'b', 'c')
p = 2 ** v
print('p = ', p)
# b is the set of all propositional valuations.
b = Set(create_valuation(m, v) for m in p)
s = [i for i in b for f in fs if evaluate(f, i)]
print('Set of all valuations satisfying all facts: ', s)
if len(s) == 1:
	i = s[0]
	offenders = [x for x in v if i[x]]
	print('Set fo offenders: ', offenders)