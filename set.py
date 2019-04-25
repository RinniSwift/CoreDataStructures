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
		return self.elements.contains(element)

	def add(self, element):
		"""adds element to set if not present already"""
		# O(1) for contains method
		if self.elements.contains(element):
			return
		else:
			self.count += 1	# increment count by one since we only read the size in the initializer
			# O(n) for setting
			self.elements.set(element, element)

	def remove(self, element):
		"""remove element from this set, if present, or else raise KeyError"""
		# O(n) for contains method
		if self.elements.contains(element):
			self.count -= 1
			# O(n) for delete
			self.elements.delete(element)
		else:
			raise KeyError('Element not in set: {}'.format(element))

	def union(self, other_set):
		"""return a new set that is the union of this set and other_set
		Union: all elements in both sets
		"""
		new_set = Set(self.elements.keys())

		for item in other_set.elements.keys():
			new_set.add(item)

		return new_set

	def intersection(self, other_set):
		"""return a new set that is the intersection of this set and other_set
		Intersection: all elements that contain in both sets
		"""
		new_set = Set()

		if self.count > other_set.count:
			print(other_set.elements.keys())
			# loop through other_set
			for element in other_set.elements.keys():
				if self.elements.contains(element):
					print("inside: {}".format(element))
					new_set.add(element)
		else:
			for element in self.elements.keys():
				if other_set.contains(element):
					new_set.add(element)
		
		return new_set

	def difference(self, other_set):
		"""return a new set that is the difference of this set and other_set
		Difference: all elements that do not contain in the other_set 
		"""
		new_set = Set(self.elements.keys())

		for key in self.elements.keys():
			if other_set.contains(key):
				new_set.remove(key)

		return new_set

	def is_subset(self, other_set):
		"""return a boolean indicating whether other_set is a subset of this set"""

		for element in other_set.elements.keys():
			if self.elements.contains(element) is False:
				return False
		return True





