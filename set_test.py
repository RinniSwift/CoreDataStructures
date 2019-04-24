
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
		with self.assertRaises(ValueError):
			s.remove('A')
		s.remove('B')
		assert s.count == 2
		
