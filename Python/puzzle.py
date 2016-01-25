from lecture import Set
from blist import blist
import copy
import time

def state_to_string(state):
	indent = ' ' * 4
	line = indent + '+-' * 3 + '+\n'
	result = '\n' + line

def find_path(start, goal, next_states):
	count = 1
	paths = Set([start])
	states = Set(start)
	explored = Set()

	while states != explored:
		time_iteration_start = time.time() 
		print('iteration number %s' % count)
		count += 1
		time_deepcopy_start = time.time()
		explored = copy.deepcopy(states)
		time_deepcopy_end = time.time() 
		global time_deepcopied
		time_deepcopied += time_deepcopy_end -time_deepcopy_start
		
		time_paths_start = time.time() 		
		paths = Set(x + [s] for x in paths for s in next_states(x[-1]) if not s in states)
		time_paths_end = time.time() 

		time_sets_add_start = time.time() 
		states += Set(p[-1] for p in paths)
		time_sets_add_end = time.time() 

		print('number of states %s' % len(states))
		
		time_goal_start = time.time() 
		if goal in states:
			return Set(l for l in paths if l[-1] == goal).arb()
		time_goal_end = time.time()
		print('time paths: 		%ss' % (time_paths_end - time_paths_start))
		print('time sets_add: 	%ss' % (time_sets_add_end - time_sets_add_start))
		print('time goal if: 	%ss' % (time_goal_end - time_goal_start))

def find_blank(state):
	return Set((row, col) for row in range(3) for col in range(3) if state[row][col]== 0).arb()

def next_states(state):
	directions = Set((1, 0), (-1 ,0), (0, 1), (0, -1))
	(row, col) = find_blank(state)
	ns = Set(move_dir(state, row, col, (dx, dy)) for (dx, dy) in directions if row + dx in [0,1,2] and col + dy in [0,1,2])
	return ns

def move_dir(state, row, col, direction):
	(dx, dy) = direction
	start_time_deeplink = time.time()
	next_state = copy.deepcopy(state)
	end_time_deeplink = time.time()

	global time_deepcopied
	time_deepcopied += end_time_deeplink - start_time_deeplink
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
	state_to_string(state)

print('total time loss due to deepcopy: %s' % time_deepcopied)
