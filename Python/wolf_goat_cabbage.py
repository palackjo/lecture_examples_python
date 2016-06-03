from lecture import Set
import copy
# There once was a farmer who wanted to cross a river with a wolf, a goat,
# and a crate of cabbage. 

# Check wether there is a path from x to y in R and compute it.
def find_path(x, y, r):
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
    length = len(Set(x for x in l1) * Set(x for x in l2))
    return length == 1

# The product call add(p,q) computes the sum of the sets p and q.
# The last point of p has to be the first point of q.
def add(p, q):
    return p + [q[1]]

#################################################
#                                               #
# Problem specific code                         #
#                                               #
#################################################

def problem(s):
    return not 'farmer' in s \
            and (('goat' in s and 'cabbage' in s) or ('wolf' in s and 'goat' in s))

wgc_all = Set('farmer', 'wolf', 'goat', 'cabbage')
p       = Set(s for s in 2 ** wgc_all if not problem(s)
                        and not problem(wgc_all - s))

r1      = Set([s, s - b] for s in p for b in 2 ** s
                    if (s - b) in p and 'farmer' in b and len(b) <= 2)
r2      = Set([y, x] for [x, y] in r1)

r       = r1 + r2
start   = wgc_all
goal    = Set()
path    = find_path(start, goal, r)

#################################################
#                                               #
# Display the code                              #
#                                               #
#################################################


def mk_pair(s):
    return [s, wgc_all - s]

# Print the path.
def print_path(p_path, total):
    for i in range(len(p_path)):
        [s1, s2] = mk_pair(p_path[i])
        if len(s1) == 0 or len(s2) == 0:
            print(s1, 33 * ' ', s2)
        else:
            print(s1, 35 * ' ', s2)
        if i == len(p_path) - 1:
            break
        [t1, t2] = mk_pair(p_path[i + 1])
        if 'farmer' in s1:
            b = s1 - t1
            print('                         >>>> ', b, ' >>>> ')
        else:
            b = s2 - t2
            print('                         <<<< ', b, ' <<<< ')

print('')
print_path(path, wgc_all)
