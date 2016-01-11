# There once was a farmer who wanted to cross a river with a wolf, a goat,
# and a crate of cabbage. 

# Check wether there is a path from x to y in R and compute it.
def find_path(x, y, r):
	p = [[x]]
	while True:
		old_p = p
		p = remove_dups(p + path_product(p, r))
		found = [l for l in p if l[-1] == y]
		if found:
			return found[0]
		if p == old_p:
			return

def path_product(p, q):
	return [add(x, y) for x in p for y in q 
			if x[-1] == y[0] and no_cycle(x, y)]

def no_cycle(l1, l2):
	return len([x for x in l1 if x in l2]) == 1

# The product call add(p,q) computes the sum of the lists p and q.
# The last point of p has to be the first point of q.
def add(p, q):
	return p + [q[1]]

def remove_dups(l):
	k = []
	[k.append(x) for x in l if x not in k]
	return k

# This method creates the power of a list.
def power_list(l):
	x = len(l)
	k = []
	for i in range(1 << x):
		k.append([l[j] for j in range(x) if (i & (1 << j))])
	return k

# This method returns the difference between k and l
def diff_list(k, l):
	return [x for x in k if x not in l]

#################################################
#												#
# Problem specific code							#
#												#
#################################################

def problem(s):
	return not('farmer' in s) and (('goat' in s and 'cabbage' in s) 
								   or ('wolf' in s and 'goat' in s))

wgc_all = ['farmer', 'wolf', 'goat', 'cabbage']
p = [s for s in power_list(wgc_all) if not problem(s)
						and not problem(diff_list(wgc_all, s))]
r1 = [[s, diff_list(s, b)] for s in p for b in power_list(s)
					if diff_list(s, b) in p and 'farmer' in b and len(b) <= 2]
r2 =[[y, x] for [x, y] in r1]
r = r1 + r2
start = wgc_all
goal = []

path = find_path(start, goal, r)
print(len(path))


#################################################
#												#
# Display the code								#
#												#
#################################################


def mk_pair(s):
	return [s, diff_list(wgc_all, s)]

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
			b = diff_list(s1, t1)
			print('                         >>>> ', b, ' >>>> ')
		else:
			b = diff_list(s2, t2)
			print('                         <<<< ', b, ' <<<< ')

print('')
print_path(path, wgc_all)
