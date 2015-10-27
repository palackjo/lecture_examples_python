class Set(Object):

	def __init__(self, data_list=None, *args):
		self.data = []
		
		if data_list:
			if not hasattr(data_list, '__iter__'):
				raise Exception('data_list parameter needs to be iterable')

			for x in data_list:
				self.insert(self.data, x)

		for arg in args:
			self.insert(self.data, arg)

		self.data.sort()

	def __add__(self, other):
		result = []
		if isinstance(other, Set):
			for x in other.data:
				self.insert(result, x)
		else:
			self.insert(result, other)

		for x in self.data:
			self.insert(result, x)

		return Set(data_list=result)

	def __mul__(self, other):
		assert isinstance(other, Set)

		result = []

		for y in self.data:
			if y in other.data:
				self.insert(result, y)

		return Set(data_list=result)

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

	def __div__(self, other):
		assert isinstance(other, Set)

		result = []

		for x in self.data:
			if x not in other.data:
				self.insert(result, x)

		return Set(data_list=result)

	def __mod__(self, other):
		assert isinstance(other, Set)

		return (self / other) + (other / self)

	def __iter__(self):
		for x in self.data:
			yield x

	# helper method to only insert elements into an array 'arr', that are
	# not present in the array (set behavior)
	def insert(self, arr, value):
		if value in arr:
			return

		arr.add(value)

	# returns a new set representing the cartesian product of the current
	# set
	def cartesian_product(self, other):
		assert isinstance(other, Set)

		result = []
		for x in self.data:
			for y in other.data:
				self.insert(result, (x,y))

		return Set(data_list=result)
