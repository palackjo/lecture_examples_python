from lecture.util import Match, is_number


def diff(t,x):
    match = Match(test=True)
    if match.match('a+b', t):
        return '{diff_a} + {diff_b}'.format(diff_a=diff(match.values['a'], x), diff_b=diff(match.values['b'], x))
    elif match.match('a-b', t):
        return '{diff_a} - {diff_b}'.format(diff_a=diff(match.values['a'], x), diff_b=diff(match.values['b'], x))
    elif match.match('a*b', t):
        return '{diff_a} * {b} + {a} * {diff_b}'.format(diff_a=diff(match.values['a'], x), b=match.values['b'], a=match.values['a'], diff_b=diff(match.values['b'], x))
    elif match.match('a/b', t):
        return '({diff_a} * {b} - {a} * {diff_b}) / {b} * {b}'.format(diff_a=diff(match.values['a'], x), diff_b=diff(match.values['b'], x), a=match.values['a'], b=match.values['b'])
    elif match.match('a**b', t):
        return diff('exp({b} * ln({a}))'.format(a=match.values['a'], b=match.values['b']), x)
    elif match.match('ln(a)', t):
        return '{diff_a} / {a}'.format(diff_a=diff(match.values['a'], x), a=match.values['a'])
    elif match.match('exp(a)', t):
        print(t)
        print(match.values['a'])
        return '{diff_a} * exp({a})'.format(diff_a=diff(match.values['a'], x), a=match.values['a'])
    elif match.is_variable(t) and t == x:
        return '1'
    elif match.is_variable(t):
        return '0'
    elif match.is_number(t):
        return '0'

def test(s):
    print('differentiating %s:' % s)
    d = diff(s, 'x')
    print(d)

test("x")
test("y")
test("1")
test("x + x")
test("x+x+y")
test("x*x")
test("x/x")
test("1/x")
test("ln(x)")
test("exp(x)")
test("x ** x")