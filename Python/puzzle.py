from lecture import Set
from blist import blist
import copy
import time

def state_to_string(state):
	indent = ' ' * 4
	line = indent + '+-' * 3 + '+\n'
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

def find_path(start, goal, next_states):
	count_iteration = 1
	count_states = 0
	paths = Set([start])
	states = Set(start)

	while len(states) != count_states:
		count_states = len(states)
		print('iteration number %s' % count_iteration)
		count_iteration += 1			
		paths = Set(x + [s] for x in paths for s in next_states(x[-1]) if not s in states)
		states += Set(p[-1] for p in paths)
		if goal in states:
			return Set(l for l in paths if l[-1] == goal).arb()
	print('result not found')

def find_blank(state):
	for row in range(3):
		for col in range(3):
			if state[row][col] == 0:
				return (row, col)

def next_states(state):
	directions = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
	(row, col) = find_blank(state)
	ns = [move_dir(state, row, col, (dx, dy)) for (dx, dy) in directions if 0 <= row + dx <= 2 and 0 <= col + dy <= 2]
	return ns

def move_dir(state, row, col, direction):
	(dx, dy) = direction
	next_state = [list(x) for x in state]
	next_state[row][col] = next_state[row + dx][col + dy]
	next_state[row + dx][col + dy] = 0
	return next_state


start = [ [8, 0, 6],
		  [5, 4, 7],
		  [2, 3, 1] ]

goal =  [ [0, 1, 2],
		  [3, 4, 5],
		  [6, 7, 8] ]

time_deepcopied = 0
path = find_path(start, goal, next_states)

for state in path:
	print(state_to_string(state))

