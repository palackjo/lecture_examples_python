from blist import sortedset
import types
import random

if __name__ == '__main__':
	from util import is_number, Sorter
else:
	from .util import is_number, Sorter

class Set():

	def __init__(self, *args, data_list=None, sorted_set=None, keep_generators=False, single_type_values=True):
		key = None
		if not single_type_values:
			key = self.gen_key
		if sorted_set:
			self.data = sortedset(sorted_set, key=key)
		else:
			self.data = sortedset([], key=key)

		if data_list:
			if not hasattr(data_list, '__iter__'):
				raise Exception('data_list parameter needs to be iterable')

			for x in data_list:
				self.data.add(x)

		for arg in args:
			if isinstance(arg, types.GeneratorType) \
			and not keep_generators: 
				for x in arg:
					self.data.add(x)
			else:
				self.data.add(arg)

	def __add__(self, other):
		
		if isinstance(other, Set):
			# union
			return Set(sorted_set=self.data | other.data)
		else:
			s = Set(sorted_set=self.data.copy())
			s.data.add(other)
			return s

	def __iadd__(self, other):
		if isinstance(other, Set):
			self.data |= other.data
		else:
			self.data.add(other)
		return self

	def __sub__(self, other):
		if isinstance(other, Set):
			return Set(sorted_set=self.data - other.data)
		else:
			s = Set(sorted_set=self.data.copy())
			s.discard(other)
			return s

	def __mul__(self, other):
		assert isinstance(other, Set)
		
		return Set(sorted_set=self.data & other.data)

	def __str__(self):
		return str(self.data)

	def __pow__(self, other):
		if other == 2:
			return self.cartesian_product(self)
		return self.cartesian_product(other)		

	def __rpow__(self, other):
		if other == 2:
			return self.cartesian_product(self)
		return self.cartesian_product(other)

	def __mod__(self, other):
		assert isinstance(other, Set)

		return Set(sorted_set=self.data ^ other.data)

	def __iter__(self):
		return self.data.__iter__()

	def __str__(self):
		return str(self.data)

	def __len__(self):
		return len(self.data)

	def __lt__(self, other):
		assert isinstance(other, Set)
		
		return self.data < other.data

	def __gt__(self, other):
		assert isinstance(other, Set)
		
		return self.data > other.data

	def __ge__(self, other):
		assert isinstance(other, Set)
		
		return self.data >= other.data

	def __le__(self, other):
		assert isinstance(other, Set)
		
		return self.data <= other.data

	def __eq__(self, other):
		return self.data <= other.data and self.data >= other.data

	def __ne__(self, other):
		return not self.__eq__(other)

	def __contains__(self, other):
		return other in self.data

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
		return self.data[random.randrange(len(self.data))]

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
