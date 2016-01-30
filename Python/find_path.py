from lecture import Set

def reachable(x, y, r):
    p = Set([x])
    while True:
        old_p = p
        p     = p + path_product(p, r)
        found = Set(l for l in p if l[-1] == y)
        if found:
            return found.arb()
        if p == old_p:
            return

def path_product(p, q):
    return Set(add(x, y) for x in p for y in q 
            if x[-1] == y[0] and no_cycle(x, y))

def no_cycle(l1, l2):
    return len([x for x in l1 if x in l2]) == 1

def add(p, q):
    return p + q[1:]

r = Set([1,2], [2,3], [1,3], [2,4], [4,5], [5,1])
print('r = ', r)
p = reachable(1, 5, r)
print('p = ', p)
