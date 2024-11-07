class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class KeyedLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, key, value):
        self.size = self.size + 1
        if self.head == None:
            self.head = Node(key, value)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(key, value)

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
    
    def find(self, key):
        current = self.head
        while current != None:
            if current.key == key:
                return current
            current = current.next
        return None
    
    def debug(self):
        current = self.head
        print('[', end='')
        while current != None:
            print(f'({current.key}, {current.value})', end='')
            current = current.next
            if current != None:
                print(',', end='')
        print(']')

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
if __name__ == "__main__":
    a = KeyedLinkedList()
    a.append("vignesh", 80)
    a.append("kumar", 80)
    a.debug()