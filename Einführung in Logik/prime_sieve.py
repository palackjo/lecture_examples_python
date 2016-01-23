# prime-sieve.stlx translation
from lecture import Set

n = 100

primes = Set(x for x in range(2, 101)) - Set((p * q) for p in range(2, 101) for q in range(2, 101) if p * q <= 100)

print(primes)