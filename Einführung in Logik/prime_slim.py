# prime-slim.stlx

def teiler(p):
	return [ x for x in range(1, p + 1) if p % x == 0 ]

n = 100
primes = [ x for x in range(2, 100 + 1) if teiler(x) == [1, x] ]
print(primes)