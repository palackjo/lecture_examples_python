# prime-sieve.stlx translation
from lecture import Set

n = 100

primes = Set(data_list=[x for x in range(2, 101)]) - Set(data_list=[(p * q) for p in range(2, 101) for q in range(2, 101) if p * q <= 100])

print(primes)