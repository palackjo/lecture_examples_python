a    = [1, 2, 3]
b    = [2, 3, 4, 5, 6]
c    = {5, 6, 7}
# Concatenating Tupels with +
print(a, '+', b, '=', a + b)
# Calculating the number of elements of a set
print('#', c, '=', len(c))
# Calculating length of a tuple
print('#', a, '=', len(a))
# Selecting the third element of b
print(b, '[2] =', b[2] )
# Overwriting the 5th element of b
b[4] = 42
print('b =', b)
# Selection of a part of a list
d    = b[2:4];
print('d =', d)
x    = 1
y    = 2
# Swapping values of x and y
[x, y] = [y, x]
print('x =', x, ', y =', y)
# Selection of the last item of b
print('b[-1] =', b[-1])
