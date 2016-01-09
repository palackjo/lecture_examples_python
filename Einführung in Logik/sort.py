def sort(s):
    return [n for n in range(1, max(s) + 1) if n in s]

s = [13, 5, 7, 2, 4]
print('sort(', s, ') = ', sort(s))
