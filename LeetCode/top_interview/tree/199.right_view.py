# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#this is correct solution using BFS approach
# done on 26-06-23
from collections import deque
class Solution:
    def rightSideView(self, root):
        res = []
        q = deque()

        if not root:
            return res
        
        q.append(root)
        while q:
            r = len(q)-1

            while r >= 0:
                if q[r]:
                    res.append(q[r].val)
                    break
                else:
                    r = r-1
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)

        return res