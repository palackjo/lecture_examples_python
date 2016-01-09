def sum_r(n):
    if n == 0:
        return 0
    else:
        return sum_r(n - 1) + n

n = int(input('Zahl eingeben: '))
total = sum_r(n)
print('Sum 0 + 1 + 2 + ... + ', n, ' = ', total)
