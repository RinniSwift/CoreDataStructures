
class CircularBuffer(object):
	def __init__(self, max_size=12):
		self.size = 0
		self.max_size = max_size
		self.elements = []

	def is_empty(self):
		if self.size == 0:
			return False
		else:
			return True

	def is_full(self):
		if self.size == max_size:
			return True
		else:
			return False

	def enqueue(self,item):
		if self.size < self.max_size:
			self.elements.append(item)
			self.size += 1

	def front(self):
		if self.size > 0:
			return self.elements[0]
		else:
			return None
		
	def dequeue(self):
		if self.size == 0:
			return None
		else:
			first = self.elements[0]
			self.elements.remove(first)
			self.size -= 1
			return first
