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

#this is a revision done on 01-08-2023
#correct solution
from collections import deque
class Solution:
    def levelOrder(self, root):
        res = []
        stack = deque()
        stack.append(root)
        if not root:
            return res

        while stack:
            level = []
            for i in range(len(stack)):
                node = stack.popleft()

                if node:
                    level.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)

            if level:
                res.append(level)
            
        return res


#revision done on 04-10-2023
class Solution:
    def levelOrder(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)

        return res
                
