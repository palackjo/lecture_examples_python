from . import is_number

"""
Deprecated sorting alternative to key sorting.
"""
class Sorter():

	def __init__(self, obj, *args):
		self.obj = obj

	def get_type_rank(self, value):
		if is_number(value):
			return 2

		if isinstance(value, str):
			return 1

		return 0

	def get_value(self, obj, deep=False):
		if is_number(obj):
			return int(obj)

		if isinstance(obj, str):
			return str(obj)

		if not deep and hasattr(obj, '__iter__'):
			try:
				return self.gen_key('_' + len(obj) + str(obj[0]), deep=True)
			except Exception:
				pass

		return '___' + type(obj).__name__

	def compare(self, other, method):
		if not self.get_type_rank(self.obj) == self.get_type_rank(other.obj):
			compare_method = getattr(int, method)
			return compare_method(self.get_type_rank(self.obj), self.get_type_rank(other.obj))

		compare_method = getattr(type(self.get_value(self.obj)), method)
		return compare_method(self.get_value(self.obj), self.get_value(other.obj))

	# self < other
	def __lt__(self, other):
		return self.compare(other, '__lt__')

	def __gt__(self, other):
		return self.compare(other, '__gt__')

	def __eq__(self, other):
		return self.compare(other, '__eq__')

	def __le__(self, other):
		return self.compare(other, '__le__')

	def __ge__(self, other):
		return self.compare(other, '__ge__')

	def __ne__(self, other):
		return self.compare(other, '__ne__')
