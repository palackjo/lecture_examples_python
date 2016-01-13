# legendre.stlx translation

from lecture import Set
from lecture.util import is_prime

def find_counter_example(1):

	def legendre(n):
		k = n * n + 1
		while k < (n + 1) ** 2:
			if is_prime(k)
				print('%s ** 2 < %s < %s ** 2' % (n**2, k, (n+1)**2))
				return True
			k++
		return False

	while True:
		if legendre(n):
			n++
		else:
			print('Legendre was wrong, no prime between %s and %s !' % (n**2, (n+1)**2))


find_counter_example(1)