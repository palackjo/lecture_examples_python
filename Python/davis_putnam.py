from lecture.util import Match
from lecture.set import Set


def davis_putnam(clauses, literals):
    s = saturate(clauses)
    if Set() in s:
        return Set(Set())
    if all(len(c) == 1 for c in s):
        return s
    l = select_literal(s, literals)
    not_l = negate_literal(l)
    r = davis_putnam(s + Set(Set(l)), literals + Set(l, not_l))
    if r != Set(Set()):
        return r
    return davis_putnam(s + Set(Set(not_l)), literals + Set(l, not_l))


def saturate(clauses):
    s = clauses
    units = Set(k for k in s if len(k) == 1)
    used = Set()
    while len(units) != 0:
        unit = units.arb()
        used += Set(unit)
        l = unit.arb()
        s = _reduce(s, l)
        temp = Set(k for k in s if len(k) == 1)
        units = temp - used
    return s


def _reduce(s, l):
    not_l = negate_literal(l)
    return Set(k - Set(not_l) for k in s if not_l in k) + \
           Set(k for k in s if not (not_l in k) and not (l in k)) + \
           Set(Set(l))


def select_literal(s, forbidden): 
    temp = s.sum() - forbidden
    temp = Set(x for x in temp if is_positive(x))
    return temp.arb()


def is_positive(l):
    match = Match()
    if match.match("!l", l):
        return False
    return True


def negate_literal(l):
    match = Match()
    if match.match("l", l):
        return '!' + match.values['l']
    if match.match("!l", l):
        return match.values['l']
    raise Exception('Cannot negate literal "%s"' % l)


if __name__ == '__main__':
    m = Set(
        Set('r', 'p', 's'),
        Set('r', 's'),
        Set('q', 'p', 's'),
        Set('!p', '!q'),
        Set('!p', 's', '!r'),
        Set('p', '!q', 'r'),
        Set('!r', '!s', 'q'),
        Set('p', 'q', 'r', 's'),
        Set('r', '!s', 'q'),
        Set('!r', 's', '!q'),
        Set('s', '!r')
    )
    print(davis_putnam(m, Set()))
