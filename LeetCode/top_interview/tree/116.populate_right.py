"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root):
        q = deque()
        q.append(root)

        while q:
            count = len(q)
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    if count > 1:
                        node.next = q[0]
                        count -= 1
                    q.append(node.left)
                    q.append(node.right)                  

        return root
