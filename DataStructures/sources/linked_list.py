class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size = self.size + 1
        if self.head == None:
            self.head = Node(data)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index error")
        self.size = self.size - 1;
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        current_index = 1
        while current_index < index:
            current = current.next
            current_index = current_index + 1
        current.next = current.next.next

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index error")
        if index == 0:
            return self.head.data
        current = self.head
        current_index = 1
        while current_index <= index:
            current = current.next
            current_index = current_index + 1
        return current.data
    
    def debug(self):
        current = self.head
        print('[', end='')
        while current != None:
            print(current.data, end='')
            current = current.next
            if current != None:
                print(',', end='')
        print(']')

    def get_size(self):
        return self.size



# Unit tests

import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Initialize an empty LinkedList before each test."""
        self.list = LinkedList()

    def test_size_empty_list(self):
        """Test size of an empty list should be 0."""
        self.assertEqual(self.list.get_size(), 0, "Size of an empty list should be 0")

    def test_append_element_increases_size(self):
        """Test that appending an element increases the size by 1."""
        initial_size = self.list.get_size()
        self.list.append(10)
        self.assertEqual(self.list.get_size(), initial_size + 1, "Size should increase by 1 after appending an element")

    def test_append_multiple_elements(self):
        """Test appending multiple elements increases size correctly."""
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.assertEqual(self.list.get_size(), 3, "Size should be 3 after appending three elements")

    def test_remove_element_at_index(self):
        """Test that removing an element by index decreases the size by 1 and shifts elements."""
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        initial_size = self.list.get_size()
        self.list.remove_at(1)  # Remove element at index 1 (value 20)
        self.assertEqual(self.list.get_size(), initial_size - 1, "Size should decrease by 1 after removing an element by index")
        self.assertEqual(self.list.get(1), 30, "Element at index 1 should now be 30 after removing previous element")

    def test_remove_element_at_invalid_index(self):
        """Test that removing an element at an invalid index raises an IndexError."""
        self.list.append(10)
        with self.assertRaises(IndexError):
            self.list.remove_at(5)  # Invalid index (out of bounds)

    def test_find_element_at_index(self):
        """Test finding elements at specific indices."""
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.assertEqual(self.list.get(0), 10, "Element at index 0 should be 10")
        self.assertEqual(self.list.get(1), 20, "Element at index 1 should be 20")
        self.assertEqual(self.list.get(2), 30, "Element at index 2 should be 30")

    def test_find_element_at_invalid_index(self):
        """Test getting an element at an invalid index raises an IndexError."""
        self.list.append(10)
        with self.assertRaises(IndexError):
            self.list.get(5)  # Index out of bounds

    def test_find_element_empty_list(self):
        """Test that finding an element in an empty list raises an IndexError."""
        with self.assertRaises(IndexError):
            self.list.get(0)  # No elements in list

if __name__ == "__main__":
    unittest.main()