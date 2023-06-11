# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head ):
        copy_map = {None : None}
        tail = head

        while tail:
            copy = Node(tail.val)
            copy_map[tail] = copy
            tail = tail.next

        tail = head

        while tail:
            copy_map[tail].next = copy_map[tail.next]
            copy_map[tail].random = copy_map[tail.random]
            tail = tail.next

        return copy_map[head]