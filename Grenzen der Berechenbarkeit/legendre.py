# This function checks whether there is a prime between the numbers n ** 2 and (n+1) ** 2.
def legendre(n):
	k = n*n + 1
	while k < (n+1) ** 2:
		if is_prime(k):
			return True
		k += 1
	return False


# Current workaround is_prime shall be implemented in the defined module.
def is_prime(n):
	return all(n % i for i in range(2, n))

# First, the number n is read. 
# Next, we have to check whether Legendre's claim is true for this number.
# If it's wrong, the function just returns and prints the counter example.
# Otherwise, n is incremented and we'll try to check, whether Legendre's claim is true for n+1.
# As long as we can't find a counter example we'll keep going.
# This example shall demonstrate, that it is generally impossible to tell if a function terminates.
# If this problem could be solved, the function would be able to solve mathematical questions.
def find_counter_example(n):
	while True:
		if legendre(n):
			print(n)
			n += 1
		else:
			print('Legendre was wrong, no prime between %d and %d!', n**2, (n+1**2))


find_counter_example(2)
