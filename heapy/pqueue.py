from heapy.util import *

class pqueue_min:
	"""
		Maintains a heap and an index mapping items to position
		in the heap (for quickly modifying item values)

		min - O(log(n))
		insert - O(log(n)) (average: O(1))
		update - O(log(n)) (average: O(1))

		Useful for:
			- Dijkstra
			- Rolling Median
			- A*
	"""

	def __init__(self, l=None):
		self._index = {}
		if l == None:
			self._l = []
		else:
			self._l = build_heap(l, self._index)

	# remove and return the min
	def pop(self, n=None):
		"""
			Remove and return the min tuple, or the tuple for the specified key.
			Returns
				tuple (key, weight)
		"""

		if len(self._l) == 0 : return None

		if n == None: # default get's the min
			i = 0
		else: # if an item is supplied, remove it
			i = self._index[n]

		m = self._l[i]
		del self._index[m[0]]

		if len(self._l) > 1:
			n = self._l.pop()
			self._l[i] = n
			self._index[n[0]] = i
			down_heapify(self._l, i, self._index) #_siftdown
		else:
			self._l.pop()


		return m

	# add an element
	def push(self, t):
		"""
			Add an element as a key weight pair.
			t - tuple (key, weight)
		"""
		# existing element?
		if t[0] in self._index:
			return self._update(t)


		self._l.append(t)
		i = len(self._l) - 1
		self._index[t[0]] = i
		up_heapify(self._l, i, self._index) #_siftup

	# return the min (without removal)
	def peek(self):
		"""Return the minimum (as a tuple), without removing it."""
		if len(self._l) == 0: return None

		return self._l[0]

	def remove(self, n):
		"""Remove the element with the specified key, and return it's tuple."""
		return self.pop(n)

	def _update(self, t):

		n = t[0]
		w = t[1]

		i = self._index[n]
		t0 = self._l[i]
		w0 = t0[1]

		if w0 == w: return

		if w < w0:
			self._l[i] = t
			up_heapify(self._l, i, self._index)
		else:
			self._l[i] = t
			down_heapify(self._l, i, self._index)

	# comtianer methods
	def __len__(self):
		return len(self._l)

	def __contains__(self, item):
		return item in self._index

	def __getitem__(self, key):
		return self._l[self._index[key]][1]

	def __setitem__(self, key, value):
		self.push((key, value))


class pqueue_max:
	"""
		Maintains a heap and an index mapping items to position
		in the heap (for quickly modifying item values)

		min - O(log(n))
		insert - O(log(n)) (average: O(1))
		update - O(log(n)) (average: O(1))

		Useful for:
			- Dijkstra
			- Rolling Median
			- A*
	"""

	def __init__(self, l=None):
		self._index = {}
		if l == None:
			self._l = []
		else:
			self._l = build_heap_max(l, self._index)

	# remove and return the min
	def pop(self, t=None):
		"""
			Returns
				tuple (item, weight)
		"""
		if len(self._l) == 0 : return None

		if t == None: # default get's the min
			i = 0
		else: # if an item is supplied, remove it
			i = self._index[t[0]]

		m = self._l[i]
		del self._index[m[0]]

		if len(self._l) > 1:
			n = self._l.pop()
			self._l[i] = n
			self._index[n[0]] = i
			down_heapify_max(self._l, i, self._index) #_siftdown
		else:
			self._l.pop()


		return m

	# add an element
	def push(self, t):
		"""
			t - tuple (item, weight)
		"""
		# existing element?
		if t[0] in self._index:
			return self._update(t)


		self._l.append(t)
		i = len(self._l) - 1
		self._index[t[0]] = i
		up_heapify_max(self._l, i, self._index) #_siftup

	# return the min (without removal)
	def peek(self):
		if len(self._l) == 0: return None

		return self._l[0]

	def _update(self, t):

		n = t[0]
		w = t[1]

		i = self._index[n]
		t0 = self._l[i]
		w0 = t0[1]

		if w0 == w: return

		if w < w0:
			self._l[i] = t
			up_heapify_max(self._l, i, self._index)
		else:
			self._l[i] = t
			down_heapify_max(self._l, i, self._index)


	# comtianer methods
	def __len__(self):
		return len(self._l)

	def __contains__(self, item):
		return item in self._index

	def __getitem__(self, key):
		return self._l[self._index[key]][1]

	def __setitem__(self, key, value):
		self.push((key, value))
