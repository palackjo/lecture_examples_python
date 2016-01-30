# stops.stlx translation

def stops(p, a):

    def f(x):
        while True:
            x += x

    e = equal(f, p, a)

    if e == 2:
        return 2
    else:
        return 1 - e
