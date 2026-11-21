class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #insert at right
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev
    
    #remove from list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        print(key)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        print(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        self.insert(self.cache[key])
