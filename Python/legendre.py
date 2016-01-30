# legendre.stlx translation

from lecture import Set
from lecture.util import is_prime

def find_counter_example(n):

    def legendre(n):
        k = n * n + 1
        while k < (n + 1) ** 2:
            if is_prime(k):
                print('%s ** 2 < %s < %s ** 2' % (n, k, (n+1)))
                return True
            k += 1
        return False

    while True:
        if legendre(n):
            n += 1
        else:
            print('Legendre was wrong, no prime between %s and %s !' % (n**2, (n+1)**2))
            return


find_counter_example(1)
