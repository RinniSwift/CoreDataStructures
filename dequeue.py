
class Dequeue(object):
	'''double-ended queue'''

	def __init__(self, iterable=None):
		"""Initialize this queue and enqueue the given items, if any."""
		self.list = list()
		self.size = 0
		# TODO: if iterable is not None
	
	def __repr__(self):
		"""Return a string representation of this deque."""
		return 'Deque({} items, front={})'.format(self.length(), self.front())

	def is_empty(self):
		"""Return True if this queue is empty, or False otherwise."""
		# runtime O(1) checking the value
		if self.size == 0:
			return True
		else:
			return False

	def length(self):
		"""Return the number of items in the deque"""
		# runtime O(1) retrieving a variable
		return self.size

	def push_front(item):
		"""Insert item at front of deque"""
		# runtime O(n) having to shift all the slots in the array back
		self.list.insert(item, 0)

	def push_back(item):
		"""Insert item at back of the deque"""
		# runtime O(1)*average
		self.list.append(item)

	def front(self):
		"""Returns item at front of deque"""
		# runtime O(1) retrieving value at an index
		return self.list[0]

	def back(self):
		"""Returns item at back of the deque"""
		# runtime O(1) retrieving value at an index
		return self.list[-1]

	def pop_front(self):
		"""Remove and return the item at the front of the deque"""
		# runtime O(n) having to shift later elements up the list
		return self.list.pop(0)

	def pop_back(self):
		"""Remove and return the item at the back of the deque"""
		# runtime O(1) removing last element doesnt have effect on other elements
		return self.list.pop(





