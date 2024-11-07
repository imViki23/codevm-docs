from keyed_linked_list import KeyedLinkedList

class HashTable:

    def __init__(self, size):
        self.buckets = [KeyedLinkedList() for _ in range(size)]

    def hash(self, key):
        checksum = 0
        for char in key:
            checksum += ord(char)
        return checksum % len(self.buckets)
    
    def set(self, key, value):
        hash_index = self.hash(key)
        content = self.buckets[hash_index].find(key)
        if content != None:
            content.value = value
            return
        self.buckets[hash_index].append(key, value)

    def get(self, key):
        hash_index = self.hash(key)
        content = self.buckets[hash_index].find(key)
        if content != None:
            return content.value
        return None
    
    def remove(self, key):
        hash_index = self.hash(key)
        self.buckets[hash_index].remove(key)

    def debug(self):
        count = 0
        for content in self.buckets:
            print(f'Bucket {count} has ', end='')
            count += 1
            content.debug()

if __name__ == "__main__":
    a = HashTable(5)
    a.set("vignesh", 5)
    a.set("kumar", 2)
    a.set("kumar", 6)
    a.set("edi", 2)
    a.debug()
    print('---------')
    print(f'Value of kumar is {a.get("kumar")}')
    a.remove("kumar")
    print('---------')
    a.debug()
    print('---------')
    print(f'Value of kumar is {a.get("kumar")}')