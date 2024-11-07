class Node:
    """Node class for linked list representation of the queue."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        if self.head == None:
            self.head = Node(data)
            return
        if self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
            return
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            raise IndexError("Illegal state: The object is not initialized.")
        self.size = self.size - 1
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if (self.head == None):
            raise IndexError("Illegal state: The object is not initialized.")
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        """Create a new queue before each test."""
        self.queue = Queue()

    def test_enqueue(self):
        """Test enqueue operation."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.get_size(), 2)
        self.assertEqual(self.queue.peek(), 1)

    def test_dequeue(self):
        """Test dequeue operation."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.get_size(), 1)
        self.assertEqual(self.queue.peek(), 2)

    def test_dequeue_empty(self):
        """Test dequeuing from an empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        """Test peek operation."""
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_peek_empty(self):
        """Test peeking from an empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_is_empty(self):
        """Test is_empty method."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_get_size(self):
        """Test get_size method."""
        self.assertEqual(self.queue.get_size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.get_size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.get_size(), 1)

if __name__ == '__main__':
    unittest.main()
