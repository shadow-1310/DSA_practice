# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# this is correct solution  with deque implementation
# done on 18-06-2023
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res