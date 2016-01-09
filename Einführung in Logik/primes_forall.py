def is_prime(p):
    return all([x in [1, p] for x in divisors(p)])

def divisors(p):
    return [t for t in range(1, p + 1) if p % t == 0]

n = 100
primes = [p for p in range(2, n + 1) if is_prime(p)]
print(primes)
