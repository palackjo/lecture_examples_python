def min_sort(l):
    if not l:
        return []
    m = min(l)
    return [m] + min_sort([x for x in l if x != m])

l = [13, 5, 13, 7, 2, 4]
print('sort(%s) = %s' %(l, min_sort(l)))
