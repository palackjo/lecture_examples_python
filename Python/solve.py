import math

x = 0.0
while True:
    old_x = x
    x     = math.cos(x)
    print(x)
    if abs(x - old_x) < 1.0e-16:
        print('x = ', x)
        break
