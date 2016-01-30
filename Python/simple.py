# simple.stlx translation

from lecture import Set

a = Set(1,2,3)
b = Set(2,3,4)

c = a + b
print('%s + %s = %s' % (a, b, c))

c = a * b
print('%s * %s = %s' % (a, b, c))

c = a - b
print('%s - %s = %s' % (a, b, c))

c = 2 ** a
print('2 ** %s = %s' % (a, c))

print('(%s in %s) = %s' % (a, b, a in b))

print('1 in %s = %s' % (a, 1 in a))
