import itertools
# The method call closure(r) computes the transitive
# closure of the binary relation r.
def trans_closure(r):
    t = r
    while True:
        old_t = t
        t = remove_dups(r + product(r, t))
        if t == old_t:
            return t

def product(r1, r2):
    return [[x, z] for [x, y] in r1 for [y, z] in r2
            if [x, y] in r1 and [y, z] in r2]
            
# This function removes duplicates of a list
def remove_dups(l):
    return [k for k,_ in itertools.groupby(l)]

r = [[1, 2], [2, 3], [1, 3], [2, 4], [4, 5]]
print('r = ', r)
print('Computing transitive closure of r')
t = trans_closure(r)
print('r+ = ', t)
