class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self,val):
        self.root = Node(val)
        self.size = 1

    def insert(self, val):
        curr = self.root
        while curr.next:
            curr = curr.next

        curr.next = Node(val)
        self.size += 1
        curr.next.next = None

    def from_array(self, nums):
        curr = self.root
        for n in nums:
            curr.next = Node(n)
            curr = curr.next
            self.size += 1

    def display(self):
        res = []
        curr = self.root
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res


l = LinkedList(5)
l.from_array([1,2,5])
# l.insert(1)
# l.insert(2)
# l.insert(5)
print(l.root.val)
print(l.display())
print(l.size)
