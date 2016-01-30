from time import time
start_time = time()
n          = 10000
primes     = [x for x in range(1, n + 1)]
for i in range(2, int(n / 2) + 1):
    if primes[i - 2] == 0:
        continue
    j = i
    while i * j <= n:
        primes[i*j - 2] = 0
        j               = j + 1
stop_time = time()
print([i for i in range(2, n + 1) if primes[i - 2] > 0])
print('Computation took %s seconds.' %(stop_time - start_time))
