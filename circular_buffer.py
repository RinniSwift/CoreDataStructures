
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
		"""push item from back of the array"""

		if self.is_empty():
			# if buffer is empty, set the last element to be the item
			self.elements[-1] = item
		else:
			# shift all items to the left of it's origianl place
			index = 0
			while index < self.max_size - 1:
				# setting the current index to be that of the item on the right
				self.elements[index] = self.elements[index + 1]
				index += 1
			# set the added items back to be the item
			self.elements[-1] = item

		# check if we are adding items to the array or simply shifting items off
		if self.size < self.max_size:
			self.size += 1

	def front(self):
		if self.size > 0:
			# calculate first item index by subtracting the total size by the amount of items in the array
			index = self.max_size - self.size
			return self.elements[index]
		else:
			# no items
			return None
		
	def dequeue(self):
		# no items to dequeue
		if self.size == 0:
			return None
		else:
			# calculate the first index and set to None
			index = self.max_size - self.size
			front = self.elements[index]
			self.elements[index] = None
			self.size -= 1
			return front

