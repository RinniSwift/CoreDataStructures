
from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

	def test_init(self):
		c = CircularBuffer()
		assert c.size == 0
		assert c.max_size == 12
		assert c.elements == []

		c = CircularBuffer(18)
		assert c.size == 0
		assert c.max_size == 18
		assert c.elements == []

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
		c = CircularBuffer()
		assert c.size == 0
		assert c.elements == []
		c.enqueue('R')
		c.enqueue('I')
		c.enqueue('N')
		assert c.elements == ['R', 'I', 'N']

	def test_dequeue(self):
		c = CircularBuffer()
		c.enqueue('R')
		c.enqueue('I')
		c.enqueue('N')
		assert c.elements == ['R', 'I', 'N']
		assert c.dequeue() == 'R'
		assert c.size == 2
		assert c.elements == ['I', 'N']
		assert c.dequeue() == 'I' 
		assert c.size == 1
		assert c.elements == ['N']
		assert c.dequeue() == 'N'
		assert c.size == 0
		assert c.dequeue() == None
		assert c.size == 0

