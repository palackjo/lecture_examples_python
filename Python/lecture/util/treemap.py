import time, random, blist

BLACK = 0
RED = 1

class TreeNode:
	def __init__(self, key, parent):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None
		self.color = None


class TreeMap:
	def __init__(self):
		self.root = None
		self.size = 0
		self.mod_count = 0

	def __len__():
		return self.size

	def get_entry(self, key):
		if key is None:
			raise TypeError

		p = self.root
		while not p is None:
			if key < p.key:
				p = p.left
			elif key > p.key:
				p = p.right
			else:
				return p
		return None

	def put(self, key):
		if key is None:
			raise TypeError

		t = self.root
		if t is None:
			self.root = TreeNode(key, None)
			self.size = 1
			self.mod_count += 1
			return None

		while not t is None:
			parent = t
			if key < t.key:
				t = t.left
			elif key > t.key:
				t = t.right
			else:
				return key

		n = TreeNode(key, parent)
		if key < parent.key:
			parent.left = n
		else:
			parent.right = n
		self._fix_after_insertion(n)
		self.size += 1
		self.mod_count += 1

	def _rotate_left(self, p):
		if p is None:
			return

		r = p.right
		p.right = r.left
		if not r.left is None:
			r.left.parent = p
		r.parent = p.parent
		if p.parent is None:
			self.root = r
		elif p.parent.left == p:
			p.parent.left = r
		else:
			p.parent.right = r
		r.left = p
		p.parent = r


	def _rotate_right(self, p):
		if p is None:
			return

		l = p.left
		p.left = l.right
		if not l.right is None:
			l.right.parent = p
		l.parent = p.parent
		if p.parent is None:
			self.root = l
		elif p.parent.right == p:
			p.parent.right = l
		else:
			p.parent.left = l
		l.right = p
		p.parent = l


	def _fix_after_insertion(self, x):
		x.color = 1

		while not x is None and not x.parent is None and x.parent.color == 1:
			x_parent = x.parent
			x_parent_parent = x.parent.parent
			if x.parent == TreeMap.left_of(x_parent_parent):
				y = TreeMap.right_of(x_parent_parent)
				if TreeMap.color_of(y) == 1:
					x_parent.color = 0
					y.color = 0
					x_parent_parent.color = 1
					x = x_parent_parent
				else:
					if x == TreeMap.right_of(x_parent):
						x = x_parent
						self._rotate_left(x)
					TreeMap.parent_of(x).color = 0
					TreeMap.set_color(TreeMap.parent_of(x.parent), 1)
					self._rotate_right(x_parent_parent)
			else:
				y = TreeMap.left_of(x_parent_parent)
				if TreeMap.color_of(y) == 1:
					x_parent.color = 0
					y.color = 0
					TreeMap.set_color(x_parent_parent, 1)
					x = x_parent_parent
				else:
					if x == TreeMap.left_of(x_parent):
						x = x_parent
						self._rotate_right(x)
						TreeMap.parent_of(x).color = 0
						TreeMap.set_color(TreeMap.parent_of(x.parent), 1)
						self._rotate_left(x_parent_parent)
					else:
						x_parent.color = 0
						TreeMap.parent_of(x_parent).color = 1
						self._rotate_left(x_parent_parent)
		self.root.color = 0

	@staticmethod
	def cmp(x, y):
		return (x > y) - (x < y)

	@staticmethod
	def parent_of(n):
		if n is None:
			return None
		else:
			return n.parent

	@staticmethod
	def left_of(n):
		return n.left if not n is None else None

	@staticmethod
	def right_of(n):
		return n.right if not n is None else None

	@staticmethod
	def color_of(n):
		return 0 if n is None else n.color

	@staticmethod
	def set_color(n, color):
		if not n is None:
			n.color = color
			

if __name__ == '__main__':
	tree = TreeMap()
	s = time.time()
	for x in range(1, 1000000):
		tree.put(x) #[random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)]
	e = time.time()
	print('tree duration: %s' % (e - s))

	sset = blist.sortedset()
	s = time.time()
	for x in range(1, 1000000):
		sset.add(x) #[random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)]
	e = time.time()
	print('blist duration: %s' % (e - s))

	nset = set()
	s = time.time()
	for x in range(1, 1000000):
		nset.add(random.randrange(1,10000))
	e = time.time()
	print('set duration: %s' % (e - s))