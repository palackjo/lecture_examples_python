import math
def solve(f, x0):
    x = x0
    for n in range(10000):
        old_x = x
        x     = f(x)
        print(x)
        if abs(old_x - x) < 1.0e-15:
            return x

def func_0(x):
    return 1/(1 + x)

print('Solution to x = cos(x): ', solve(math.cos, 0))
print('Solution to x = 1/(1 + x): ', solve(func_0, 0.0))
