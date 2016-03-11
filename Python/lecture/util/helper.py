# Checks if the given parameter s is a number
def is_number(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
    	return False

# This helps to speed up the algorithm
some_primes = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
               43,  47, 53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
               173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
               241, 251, 257, 263, 269, 271, 277, 281]

some_primes_squared = [i * i for i in some_primes]

def is_prime(n):
    if n <= 1 or type(n) is not int:
        return False

    for i in range(len(some_primes)):
        if n % some_primes[i] == 0:
            return n == some_primes[i]
        elif some_primes_squared[i] >= n:
            return True

    j = some_primes[-1] + 2
    while j * j <= n:
        if n % j == 0:
            return False
        j += 2

    return True

# Simulates setlx' match behavior
def match():
	pass 