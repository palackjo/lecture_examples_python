# This program reads a number n and computes the sum 1 + 2 + ... + n
n = int(input('Type a natural number and press return: '))
s = sum(range(n + 1))
print('The sum 1 + 2 + ... + ', n, ' is equal to ', s, '.')
