from blist import sortedset

if __name__ == '__main__':
	from util import is_number, Sorter
else:
	from .util import is_number, Sorter

class Set():

	def __init__(self, *args, data_list=None):
		self.data = sortedset([], key=self.gen_key)
		
		if data_list:
			if not hasattr(data_list, '__iter__'):
				raise Exception('data_list parameter needs to be iterable')

			for x in data_list:
				self.data.add(x)

		for arg in args:
			self.data.add(arg)

	def __add__(self, other):
		s = Set()
		if isinstance(other, Set):
			for x in other.data:
				s.data.add(x)
		else:
			s.data.add(other)
		for x in self.data:
			s.data.add(x)
		return s

	def __sub__(self, other):
		s = Set()
		if isinstance(other, Set):
			for x in self.data:
				if not x in other.data:
					s.data.add(x)
		else:
			for x in self.data:
				if not x == other:
					s.data.add(x)
		return s

	def __mul__(self, other):
		assert isinstance(other, Set)
		s = Set()
		for x in self.data:
			if x in other.data:
				s.data.add(x)
		return s

	def __truediv__(self, other):
		assert isinstance(other, Set)
		s = Set()
		for x in self.data:
			if x not in other.data:
				s.data.add(x)
		return s


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
		return (self / other) + (other / self)

	def __iter__(self):
		return self.data.__iter__()

	def __str__(self):
		return "[%s]" % (', '.join([str(x) for x in self.data]))

	def __len__(self):
		return len(self.data)

	def __le__(self, other):
		assert isinstance(other, Set)
		for x in self.data:
			if not x in other.data:
				return False
		return True

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

	def pop(self):
		import random
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
	s5 = s / s1
	s6 = s % s1

	print("s: %s" % s)
	print("s1: %s" % s1)
	print("s + s1: %s" % s2)
	print("s ** 2: %s" % s ** 2)
	print("2 ** s: %s" % 2 ** s)
	print("s + s1 - s: %s" % s3)
	print("s * s1: %s" % s4)
	print("s / s1: %s" % s5)
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
