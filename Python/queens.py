import timeit

from lecture import Set
from davis_putnam import davis_putnam

def at_most_one(s):
    return Set(Set("!" + p, "!" + q) for p in s for q in s if p != q)

def at_most_one_in_row(row, n):
    return at_most_one(Set("varr%sc%s" % (str(row), str(column)) for column in range(n)))

def one_in_column(column, n):
    return Set(Set("varr%sc%s" % (str(row), str(column)) for row in range(n)))

def at_most_one_in_lower_diagonal(k, n):
    return at_most_one(
        Set(
            "varr%sc%s" % (str(row), str(column))
            for row in range(n)
            for column in range(n)
            if row - column == k
        )
    )

def at_most_one_in_upper_diagonal(k, n):
    return at_most_one(
        Set(
            "varr%sc%s" % (str(row), str(column))
            for row in range(n)
            for column in range(n)
            if row + column == k
        )
    )

def all_clauses(n):
    return Set(at_most_one_in_row(row, n)           for row in range(n)).sum() + \
           Set(at_most_one_in_lower_diagonal(k, n)  for k in range(-(n-2), n-2)).sum() + \
           Set(at_most_one_in_upper_diagonal(k, n)  for k in range(3, 2*n - 1)).sum() + \
           Set(one_in_column(column, n)             for column in range(n)).sum()

def print_board(i, n):
    if i == Set(Set()):
        return
    print("        " + ((8*n+1) * "-"))
    for row in range(n):
        line = "        |"
        for col in range(n):
            line += "       |"
        print(line)
        line = "        |"
        for col in range(n):
            if Set("varr%sc%s" % (row, col)) in i:
                line += "   Q   |"
            else:
                line += "       |"
        print(line)
        line = "        |"
        for col in range(n):
            line += "       |"
        print(line)
        print("        " + ((8*n+1) * "-"))


def solve(n):
    clauses = all_clauses(n)
    print(clauses)
    solution = davis_putnam(clauses, Set())
    if solution != Set(Set()):
        print_board(solution, n)
    else:
        print("The problem is not solvable for %s queens!" % str(n))
        print("Try to increase the number of queens.")



start_time   = timeit.default_timer()
solve(5)
stop_time    = timeit.default_timer()

time_elapsed = stop_time - start_time
print('Time used: %s seconds.' % time_elapsed)