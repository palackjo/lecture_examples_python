from lecture import Set

def trans_closure(r):
    p = r
    while True:
        old_p = p
        p = r + path_product(r, p)
        print(p)
        if p == old_p:
            return p

def path_product(p, q):
    return Set(add(x, y) for x in p for y in q if x[-1] == y[0])

def add(p, q):
    return p + q[1:]

r = Set([1,2], [2,3], [1,3], [2,4], [4,5], [5,1])
print('r = ', r)
print('computing all paths')
p = trans_closure(r)
print('p = ', p)
