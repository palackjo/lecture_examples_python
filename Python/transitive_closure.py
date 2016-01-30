from lecture import Set

# The function call trans_closure(r) computes the transitive closure
# of the binary relation r.
def trans_closure(r):
    t = r
    while True:
        old_t = t
        t     = r + product(r, t)
        if t == old_t:
            return t

def product(r1, r2):
    return Set([x, z] for [x, y] in r1 for [y, z] in r2 
            if [x, y] in r1 and [y, z] in r2)

r = Set([1,2], [2,3], [1,3], [2,4], [4,5])
print('r  =', r)
t = trans_closure(r)
print('r+ =', t)
