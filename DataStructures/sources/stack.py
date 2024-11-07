class Node:
    """Node class for linked list representation of the queue."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size+=1

    def pop(self):
        if self.head == None:
            raise IndexError("IndexError")
        head_node = self.head
        self.head = self.head.next
        self.size-=1
        return head_node.data
    
    def get_size(self):
        return self.size
    
    def peek(self):
        if self.head == None:
            raise IndexError("IndexError")
        return self.head.data
    
    def is_empty(self):
        return self.size == 0

# Unit tests

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        # Initialize a new Stack instance before each test
        self.stack = Stack()

    def test_push(self):
        # Test the push method
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_size(), 3)
        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self):
        # Test the pop method
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())
        # Check that popping from an empty stack raises an error
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        # Test the peek method
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)  # Top element should be 2
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)  # Now top element should be 1
        # Check that peeking from an empty stack raises an error
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_size(self):
        # Test the size method
        self.assertEqual(self.stack.get_size(), 0)  # Size should be 0 initially
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_size(), 2)  # After two pushes, size should be 2
        self.stack.pop()
        self.assertEqual(self.stack.get_size(), 1)  # After one pop, size should be 1

    def test_is_empty(self):
        # Test the is_empty method
        self.assertTrue(self.stack.is_empty())  # Should be empty initially
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())  # Should not be empty after one push
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())  # Should be empty after popping all elements

if __name__ == '__main__':
    unittest.main()
