
from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

	def test_init(self):
		c = CircularBuffer()
		assert c.size == 0
		assert c.max_size == 12
		assert c.elements == [None, None, None, None, None, None, None, None, None, None, None, None]
		c = CircularBuffer(4)
		assert c.size == 0
		assert c.max_size == 4
		assert c.elements == [None, None, None, None]

	def test_is_empty(self):
		c = CircularBuffer()
		assert c.is_empty() == True
		c.enqueue('A')
		assert c.is_empty() == False

	def test_is_full(self):
		c = CircularBuffer(4)
		c.enqueue('A')
		assert c.is_full() == False
		assert c.size == 1
		c.enqueue('B')
		assert c.is_full() == False
		assert c.size == 2
		c.enqueue('C')
		assert c.is_full() == False
		assert c.size == 3
		c.enqueue('D')
		assert c.is_full() == True
		assert c.size == 4

	def test_enqueue(self):
		c = CircularBuffer(6)
		assert c.size == 0
		assert c.elements == [None, None, None, None, None, None]
		c.enqueue('R')
		c.enqueue('I')
		c.enqueue('N')
		assert c.elements == [None, None, None, 'R', 'I', 'N']
		assert c.size == 3
		new = CircularBuffer(4)
		new.enqueue('A')
		new.enqueue('B')
		new.enqueue('C')
		new.enqueue('D')
		assert new.elements == ['A', 'B', 'C', 'D']
		assert new.is_full() == True
		assert new.size == 4
		new.enqueue('E')
		assert new.elements == ['B', 'C', 'D', 'E']
		assert new.size == 4

	def test_front(self):
		c = CircularBuffer(4)
		c.enqueue('R')
		c.enqueue('I')
		c.enqueue('N')
		assert c.front() == 'R'
		c.dequeue()
		assert c.front() == 'I'
		c.dequeue()
		assert c.front() == 'N'
		c.dequeue()
		assert c.front() == None

	def test_dequeue(self):
		c = CircularBuffer(6)
		c.enqueue('R')
		c.enqueue('I')
		c.enqueue('N')
		assert c.size == 3
		assert c.elements == [None, None, None, 'R', 'I', 'N']
		assert c.dequeue() == 'R'
		assert c.size == 2
		assert c.elements == [None, None, None, None, 'I', 'N']
		assert c.dequeue() == 'I' 
		assert c.size == 1
		assert c.elements == [None, None, None, None, None, 'N']
		assert c.is_empty() == False
		assert c.dequeue() == 'N'
		assert c.size == 0
		assert c.elements == [None, None, None, None, None, None]
		assert c.dequeue() == None
		assert c.size == 0
		assert c.is_empty() == True

		new = CircularBuffer(4)
		new.enqueue('A')
		new.enqueue('B')
		new.enqueue('C')
		new.enqueue('D')
		assert new.elements == ['A', 'B', 'C', 'D']
		assert new.dequeue() == 'A'
		assert new.elements == [None, 'B', 'C', 'D']
		new.enqueue('E')
		new.enqueue('F')
		assert new.elements == ['C', 'D', 'E', 'F']
		assert new.dequeue() == 'C'
		assert new.dequeue() == 'D'
		assert new.elements == [None, None, 'E', 'F']