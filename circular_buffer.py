
class CircularBuffer(object):
	def __init__(self, max_size=12):
		self.size = 0
		self.max_size = max_size
		self.elements = [None]*max_size

	def is_empty(self):
		if self.size == 0:
			return True
		else:
			return False

	def is_full(self):
		if self.size == self.max_size:
			return True
		else:
			return False

	def enqueue(self,item):
		"""insert at back of the array"""

		if self.is_empty():
			# if buffer is empty, set the last element to be the item
			self.elements[-1] = item
		else:
			# shift all items to the left of it's origianl place
			index = 0
			while index < self.max_size - 1:
				self.elements[index] = self.elements[index + 1]
				index += 1
			self.elements[-1] = item

		# check if we are adding items to the array or it's simply full and we're just shifting items off
		if self.size < self.max_size:
			self.size += 1
		


	def front(self):
		if self.size > 0:
			for item in self.elements:
				if item != None:
					return item
		else:
			return None
		
	def dequeue(self):
		if self.size == 0:
			return None
		else:
			index = self.max_size - self.size
			front = self.elements[index]
			self.elements[index] = None
			self.size -= 1
			print("front: {}".format(front))
			return front

