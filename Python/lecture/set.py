import types
import random

if __name__ == '__main__':
	from util import is_number, Sorter, TreeMap
else:
	from .util import is_number, Sorter, TreeMap

class Set():

	def __init__(self, *args, keep_generators=False):
		self.map = TreeMap()

		for arg in args:
			if isinstance(arg, types.GeneratorType) \
			and not keep_generators: 
				for x in arg:
					self.map.put(x)
			else:
				self.map.put(arg)

	def __add__(self, other):
		raise NotImplemented()

	def __iadd__(self, other):
		assert isinstance(other, Set)

		self.map += other.map
		return self

	def __sub__(self, other):
		raise NotImplemented()

	def __mul__(self, other):
		assert isinstance(other, Set)
		
		raise NotImplemented()

	def __str__(self):
		raise NotImplemented()

	def __pow__(self, other):
		raise NotImplemented()

	def __rpow__(self, other):
		raise NotImplemented()

	def __mod__(self, other):
		raise NotImplemented()

	def __iter__(self):
		return self.map.__iter__()

	def __len__(self):
		return self.map.size

	def __lt__(self, other):
		assert isinstance(other, Set)
		
		return self.map < other.map

	def __gt__(self, other):
		assert isinstance(other, Set)
		
		return self.map > other.map

	def __ge__(self, other):
		assert isinstance(other, Set)
		
		return self.map >= other.map

	def __le__(self, other):
		assert isinstance(other, Set)
		
		return self.map <= other.map

	def __eq__(self, other):
		assert isinstance(other, Set)

		return self.map == other.map

	def __ne__(self, other):
		return self.map != other.map

	def __contains__(self, other):
		if isinstance(other, Set):
			return other.map in self.map
		return other in self.map

	# returns a new set representing the cartesian product of the current
	# set
	def cartesian_product(self, other):
		assert isinstance(other, Set)
		s = Set()
		for x in self.data:
			for y in other.data:
				s.data.add((x,y))
		return s

	def arb(self):
		return self.map.get_first_entry().key #[random.randrange(len(self.data))]

	def pop(self):
		return self.data.pop(random.randrange(len(self.data)))

	def gen_key(self, value):
			return Sorter(value)
		

if __name__ == '__main__':
	dl = [[x, x ** 2] for x in range(1,10)]
	dl.append([1,2,3,4])
	s = Set([1, 1],2,2,2,2,3,4)
	s1 = Set(data_list=dl)
	s2 = s + s1
	s3 = s2 - s
	s4 = s * s1
	#s5 = s / s1
	s6 = s % s1

	print("s: %s" % s)
	print("s1: %s" % s1)
	print("s + s1: %s" % s2)
	print("s ** 2: %s" % s ** 2)
	print("2 ** s: %s" % 2 ** s)
	print("s + s1 - s: %s" % s3)
	print("s * s1: %s" % s4)
	#print("s / s1: %s" % s5)
	print("s %% s1: %s" % s6)

	print("-----------")
	for x in s:
		print(x)
	print("-----------")

	assert [1, 1] in s

	print("[1, 1] in s: True")

	s7 = Set([1, 1], 2, 3)

	assert s7 <= s

	print("s <= s7: True")

	print("Random pop: %s" % s.pop())
	print("s: %s" % s)
