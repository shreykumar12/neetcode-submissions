class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #insert to the right
    def insert(self, node):
        tmp = self.right.prev
        self.right.prev = node
        node.prev = tmp
        tmp.next = node
        node.next = self.right
    
    def remove(self, node):
        tmp = node.prev
        tmp.next = node.next
        node.next.prev = tmp
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
        else:
            self.cache[key] = Node(key, value)
            if len(self.cache) > self.cap:
                lru = self.left.next
                print(self.left.next.val)
                self.remove(lru)
                print(self.left.next.val)
                del self.cache[lru.key]
        self.insert(self.cache[key])
