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



#this rrevision done on 03-10-2023 midnight after 5-6 attempts on LC, there was problem on put method
class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self,capacity):
        self.cache = {}
        self.cap = capacity
        self.curr = 0
        self.lru = Node(0,0)
        self.mru = Node(0,0)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert(self, node):
        temp = self.mru.prev
        self.mru.prev = node
        temp.next = node
        node.prev = temp
        node.next = self.mru

    def remove(self,node):
        temp1 = node.prev
        temp2 = node.next
        temp1.next = temp2
        temp2.prev = temp1

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]    
