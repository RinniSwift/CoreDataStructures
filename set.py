#!python

from hashtable import HashTable

class Set(object):

	def __init__(self, elements=None):
		self.elements = HashTable()	# set is imlemented as a hashtable

		if elements is not None:
			for element in elements:
				if self.elements.contains(element):
					continue
				else:
					self.elements.set(element, element)

		self.count = self.elements.size	# number of items in the set (built with a hashtable)
	
	def contains(self, element):
		"""returns a boolean indicating whether element is in this set"""
		if self.elements.contains(element):
			return True
		else:
			return False

	def add(self, element):
		"""adds element to set if not present already"""
		if self.elements.contains(element):
			return
		else:
			self.count += 1	# increment count by one since we only read the size in the initializer
			self.elements.set(element, element)

	def remove(self, element):
		"""remove element from this set, if present, or else raise KeyError"""
		if self.elements.contains(element):
			self.count -= 1
			self.elements.delete(element)
		else:
			raise KeyError('Element not in set: {}'.format(element))