class Node:
    def __init__(self,key = 0,  val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        #left = LRU, right = MRU
        self.left = Node()
        self.right = Node()
        #connecting the extreame nodes
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val 
        
        return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
