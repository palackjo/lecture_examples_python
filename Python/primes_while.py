n      = 100
primes = []
p      = 2
while p <= n:
    if all([p % t != 0 for t in primes]):
        print(p)
        primes += [p]
        # primes = primes + [p]
    p += 1
    # p = p + 1
