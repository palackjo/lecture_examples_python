# from.stlx translation

from lecture import Set

def printSet(s):
	if(len(s) == 0):
		return

	x = s.pop()
	print(x)
	printSet(s)

s = Set(13, 5, 7, 2, 4)
printSet(s)