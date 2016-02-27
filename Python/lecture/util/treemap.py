import time, random, blist, copy

BLACK = 0
RED = 1


class TreeNode:
	def __init__(self, key, parent):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None
		self.color = None

	def get_next(self):
		if self.right is not None:
			p = self.right
			while p.left is not None:
				p = p.left
			return p
		else:
			p = self.parent
			ch = self
			while p is not None and ch == p.right:
				ch = p
				p = p.parent
			return p

	def successor(self):
		if self.right is not None:
			p = self.right
			while p.left is not None:
				p = p.left
			return p
		else:
			p = self.parent
			ch = self
			while p is not None and ch == p.right:
				ch = p
				p = p.parent
			return p

class TreeMap:
	def __init__(self):
		self.root = None
		self.size = 0
		self.mod_count = 0

	def __len__():
		return self.size

	def __contains__(self, other):
		if other is None:
			raise TypeError

		if isinstance(other, TreeMap):
			return self.contains_all(other)
		else:
			return self.contains(other)

	def __iter__(self):
		self.next = self.get_first_entry()
		return self

	def __eq__(self, other):
		assert isinstance(other, TreeMap)

		if self.size != other.size:
			return False
		
		if not other.contains_all(self) or not self.contains_all(other):
			return False
		return True

	def __ne__(self, other):
		assert isinstance(other, TreeMap)

		return not self == other

	def __le__(self, other):
		assert isinstance(other, TreeMap)

		return other.contains_all(self)

	def __ge__(self, other):
		assert isinstance(other, TreeMap)

		return self.contains_all(other)

	def __lt__(self, other):
		assert isinstance(other, TreeMap)

		return self <= other and self != other

	def __gt__(self, other):
		assert isinstance(other, TreeMap)

		return self >= other and self != other

	def __add__(self, other):
		assert isinstance(other, TreeMap)

		tree = TreeMap()
		# actually deepcoping the already 
		for x in self:
			tree.put(x)
		for x in other:
			tree.put(x)

		return tree


	def __iadd__(self, other):
		assert isinstance(other, TreeMap)

		for x in other:
			self.put(x)
		return self

	def __next__(self):
		if self.next is None:
			raise StopIteration
		t = self.next
		self.next = t.get_next()
		return t.key

	def get_first_entry(self):
		p = self.root
		if p is not None:
			while p.left is not None:
				p = p.left
		return p

	def get_last_entry(self):
		p = self.root
		if p is not None:
			while p.right is not None:
				p = p.right
		return p

	def contains(self, key):
		p = self.root
		while not p is None:
			if key < p.key:
				p = p.left
			elif key > p.key:
				p = p.right
			else:
				return True
		return False

	def contains_all(self, other):
		for x in other:
			if not self.contains(x):
				return False
		return True

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

	def remove(self, key):
		entry = self.get_entry(key)
		if entry is not None:
			self.delete_entry(entry)

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
		self.fix_after_insertion(n)
		self.size += 1
		self.mod_count += 1

	def delete_entry(self, p):
		self.mod_count += 1
		self.size -= 1
		if p.left is not None and p.right is not None:
			s = p.successor()
			p = s
		replacement = p.left if p.left is not None else p.right
		if replacement is not None:
			replacement.parent = p.parent
			if p.parent is None:
				root = replacement
			elif p == p.parent.left:
				p.parent.left = replacement
			else:
				p.parent.right = replacement
			p.left = p.right = p.parent = None
			if p.color == 0:
				self.fix_after_deletion(replacement)
		elif p.parent == None:
			self.root = None
		else:
			if p.color == 0:
				self.fix_after_deletion(p)
			if p.parent.left == p:
				p.parent.left = None
			elif p.parent.right == p:
				p.parent.right = None
			p.parent = None

	def rotate_left(self, p):
		# checked for none before
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

	def rotate_right(self, p):
		# checked for none before
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

	def fix_after_deletion(self, x):
		while not x.parent is None and x.color == 0:
			if x == x.parent.left:
				sib = x.parent.right
				if sib is not None and sib.color == 1:
					sib.color = 0
					x.parent.color = 1
					self.rotate_left(x.parent)
					sib = x.parent.right
				right_black = sib is not None and sib.right is not None and sib.right.color == 0
				if sib is not None and sib.left is not None and sib.left.color == 0 and right_black:
					sib.color = 1
					x = x.parent
				else:
					if right_black:
						if sib.left is not None:
							sib.left.color = 0
						sib.color = 1
						self.rotate_right(sib)
						sib = x.parent.right
					if sib is not None:
						sib.color = x.parent.color
						if sib.right is not None:
							sib.color = 0
					x.parent.color = 0
					self.rotate_left(x.parent)
					x = self.root
			else:
				sib = x.parent.left
				if sib is not None and sib.color == 1:
					sib.color = 0
					x.parent.color = 1
					self.rotate_right(x.parent)
					sib = x.parent.left
				left_black = sib is not None and sib.left is not None and sib.right.color == 0
				if sib is not None and sib.right is not None and sib.right.color == 0 and left_black:
					sib.color = 1
					x = x.parent
				else:
					if left_black:
						if sib.right is not None:
							sib.right.color = 0
						sib.color = 1
						self.rotate_left(sib)
						sib = x.parent.left
					if sib is not None:
						sib.color = x.parent.color
						if sib.left is not None:
							sib.color = 0
					x.parent.color = 0
					self.rotate_right(x.parent)
					x = self.root
		x.color = 0


	def fix_after_insertion(self, x):
		x.color = 1
		while not x is None and not x.parent is None and x.parent.color == 1:
			x_parent = x.parent
			x_parent_parent = x.parent.parent
			if not x_parent_parent is None and x_parent == x_parent_parent.left:
				y = x_parent_parent.right
				if not y is None and y.color == 1:
					x_parent.color = 0
					y.color = 0
					x_parent_parent.color = 1
					x = x_parent_parent
				else:
					if x == x_parent.right:
						x = x_parent
						self.rotate_left(x)
						# recheck parent. it might have changed.
						if not x.parent is None:
							x.parent.color = 0
							if not x.parent.parent is None:
								x.parent.parent.color = 1
								self.rotate_right(x.parent.parent)
					else:
						x_parent.color = 0
						x_parent_parent.color = 1
						self.rotate_right(x_parent_parent)
			else:
				if x_parent_parent is None:
					if x == x_parent.left:
						x = x_parent
						self.rotate_right(x)
					else:
						x_parent.color = 0
				else:
					y = x_parent_parent.left
					if not y is None and y.color == 1:
						x_parent.color = 0
						y.color = 0
						x_parent_parent.color = 1
						x = x_parent_parent
					else:
						if x == x_parent.left:
							x = x_parent
							self.rotate_right(x)
							if not x.parent is None:
								x.parent.color = 0
								if not x.parent.parent is None:
									x.parent.parent.color = 1
									self.rotate_left(x.parent.parent)
						else:
							x.parent.color = 0
							x.parent.parent.color = 1
							self.rotate_left(x.parent.parent)				
		self.root.color = 0
			

if __name__ == '__main__':
	tree = TreeMap()
	s = time.time()
	for x in range(1, 1000000):
		tree.put(x) #[random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)]
	e = time.time()
	print('insert tree duration: %s' % (e - s))

	s = time.time()
	tree = copy.deepcopy(tree)
	e = time.time()
	print('deepcopy tree duration: %s' % (e - s))

	s = time.time()
	for x in tree:
		pass
	e = time.time()
	print('iterate tree duration: %s' % (e - s))

	tree2 = TreeMap()
	s = time.time()
	for x in range(1, 1000000):
		tree2.put(x) #[random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)]
	e = time.time()
	print('insert tree2 duration: %s' % (e - s))

	s = time.time()
	print(tree2 in tree)
	e = time.time()
	print('tree2 in tree duration: %s' % (e - s))

	sset = blist.sortedset()
	s = time.time()
	for x in range(1, 1000000):
		sset.add(x) #[random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)]
	e = time.time()
	print('insert blist duration: %s' % (e - s))

	s = time.time()
	for x in sset:
		pass
	e = time.time()
	print('iterate blist duration: %s' % (e - s))

	nset = set()
	s = time.time()
	for x in range(1, 1000000):
		nset.add(random.randrange(1,10000))
	e = time.time()
	print('set duration: %s' % (e - s))