# This program solves the eight-puzzle.
from lecture import Set
import timeit

# This function converts the current state of the puzzle to a string.
def state_to_string(state):
    indent = ' ' * 4
    line   = indent + '+-' * 3 + '+\n'
    result = '\n' + line
    for row in range(3):
        result += indent + '|'
        for col in range(3):
            cell = state[row][col]
            if cell > 0:
                result += str(cell)
            else:
                result += ' '
            result += '|'
        result += '\n'
        result += line
    return result

# This function finds a path from start to goal using the function next_state.
# 1. start is the state where the search starts.
# 2. goal  is the state we want to reach.
# 3. next_state is a function that takes a state s and computes the set of all
#    states that are reachable from s in one step.
def find_path(start, goal, next_states):
    count_iteration = 1
    count_states    = 0
    paths           = Set([start])
    states          = Set(start)
    while len(states) != count_states:
        count_states = len(states)
        print('Iteration number %s' % count_iteration)
        count_iteration += 1            
        paths = Set(x + [s] 
                    for x in paths for s in next_states(x[-1]) 
                    if not s in states)
        states += Set(p[-1] for p in paths)
        print('Number of states: %s' % len(states))
        if goal in states:
            return Set(l for l in paths if l[-1] == goal).arb()

# Given a state s, compute the list of all states reachable from s.
# The state is represented as an 3 times 3 array of numbers, where the empty
# place is represented as the number 0.  The array is itself represented as
# a list of lists, where each inner list represents a row of the array.
def next_states(state):
    directions = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
    (row, col) = find_blank(state)
    ns         = [move_dir(state, row, col, (dx, dy)) 
                  for (dx, dy) in directions 
                  if 0 <= row + dx <= 2 and 0 <= col + dy <= 2]
    return ns

def move_dir(state, row, col, direction):
    (dx, dy)   = direction
    next_state = [list(x) for x in state]
    next_state[row][col] = next_state[row + dx][col + dy]
    next_state[row + dx][col + dy] = 0
    return next_state

def find_blank(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return (row, col)

start_time   = timeit.default_timer()

start = [ [8, 0, 6],
          [5, 4, 7],
          [2, 3, 1] ]

goal  = [ [0, 1, 2],
          [3, 4, 5],
          [6, 7, 8] ]

path  = find_path(start, goal, next_states)
stop_time    = timeit.default_timer()

time_elapsed = stop_time - start_time

if path:
    print('Number of steps to solve the puzzle: %s' % (len(path) - 1))
    for state in path:
        print(state_to_string(state))
else:
    print('No solution found.')

print('Time used: %s seconds.' % time_elapsed)
