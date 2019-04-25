
from set import Set
import unittest

class SetTest(unittest.TestCase):

	def test_init(self):
		s = Set()
		assert s.count == 0
		s_two = Set(['R', 'I', 'N'])
		assert s_two.count == 3
		s_two = Set(['R', 'I', 'N', 'N', 'I'])
		assert s_two.count == 3

	def test_contains(self):
		s = Set(['A', 'B', 'C'])
		assert s.contains('A') == True
		assert s.contains('B') == True
		assert s.contains('C') == True
		assert s.contains('D') == False
		assert s.contains('E') == False
		assert s.count == 3

	def test_add(self):
		s = Set()
		s.add('R')
		assert s.count == 1
		assert s.contains('R') == True
		s.add('I')
		assert s.count == 2
		assert s.contains('I') == True
		s.add('I')
		assert s.count == 2
		assert s.contains('I') == True

		s_two = Set(['R', 'I', 'N'])
		s_two.add('N')
		assert s_two.count == 3
		s_two.add('S')
		assert s_two.count == 4
		s_two.add('A')
		assert s_two.count == 5
		s_two.add('R')
		assert s_two.count == 5

	def test_remove(self):
		s = Set(['A', 'B', 'C', 'D'])
		assert s.count == 4
		s.remove('A')
		assert s.count == 3
		with self.assertRaises(KeyError):
			s.remove('A')
		s.remove('B')
		assert s.count == 2
		
	def test_union(self):
		s1 = Set(['A', 'B', 'C'])
		s2 = Set(['D', 'E', 'B'])
		new_set = s1.union(s2)
		assert new_set.count == 5
		assert new_set.contains('A') == True
		assert new_set.contains('B') == True
		assert new_set.contains('C') == True
		assert new_set.contains('D') == True
		assert new_set.contains('E') == True

		set1 = Set()
		set2 = Set(['A', 'B', 'C'])
		new_sec_set = set1.union(set2)
		assert new_sec_set.count == 3
		assert new_sec_set.contains('A')
		assert new_sec_set.contains('B')
		assert new_sec_set.contains('C')

		set_one = Set(['A', 'B', 'C'])
		set_two = Set()
		new_third_set = set_one.union(set_two)
		assert new_sec_set.count == 3
		assert new_sec_set.contains('A')
		assert new_sec_set.contains('B')
		assert new_sec_set.contains('C')

	def test_intersection(self):
		s1 = Set(['A', 'B', 'C'])
		s2 = Set(['B', 'C', 'D'])
		new_set1 = s1.intersection(s2)
		assert new_set1.count == 2
		set1 = Set(['A', 'B', 'C'])
		set2 = Set(['C', 'D', 'E', 'F'])
		new_set2 = set1.intersection(set2)
		assert new_set2.count == 1

	def test_difference(self):
		s1 = Set(['A', 'B', 'C'])
		s2 = Set(['B', 'C', 'D'])
		new_set1 = s1.difference(s2)
		assert new_set1.count == 1
		assert new_set1.contains('A')
		set1 = Set(['A', 'B', 'C', 'D'])
		set2 = Set(['C', 'D', 'E', 'F'])
		new_set2 = set1.difference(set2)
		assert new_set2.count == 2
		assert new_set2.contains('A')
		assert new_set2.contains('B')


