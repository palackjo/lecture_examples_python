n = 1000
primes = [x for x in range(2, n + 1)]
for i in range(2, int(n/2) + 1):
    j = 2
    while i * j <= n:
        primes[i*j - 2] = 'not prime'
        j = j + 1

print([i for i in range(2, n + 1) if primes[i - 2] == i])
