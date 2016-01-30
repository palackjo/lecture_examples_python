values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits  = ['c', 'h', 'd', 's']
deck   = [[v, s] for v in values for s in suits]
hole   = [['3', 'c'], ['3', 's']]
rest   = [x for x in deck if x not in hole]
flops  = [[k1, k2, k3] for k1 in rest for k2 in rest for k3 in rest
                      if k1 not in [k2, k3] and k2 != k3]
trips  = [f for f in flops if ['3', 'd'] in f or ['3', 'h'] in f]
print(1.0 * len(trips) / len(flops))
