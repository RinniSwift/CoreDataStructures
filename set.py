
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

