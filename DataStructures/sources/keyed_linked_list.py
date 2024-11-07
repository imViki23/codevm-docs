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

    def remove(self, key):
        prev = None
        current = self.head
        while current != None:
            if current.key == key:
                if prev == None:
                    self.head = None
                else:
                    prev.next = current.next
            prev = current
            current = current.next
    
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
            print(f'({current.key} = {current.value})', end='')
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
    a.append("muthu", 80)
    a.append("kumar", 80)
    a.debug()
    a.remove("muthu")
    a.debug()