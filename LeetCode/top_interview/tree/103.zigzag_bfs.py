from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return root
        
        q = deque()
        q.append(root)
        flag = True

        while q:
            level = []
            for i in range(len(q)):
                if flag:
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                else:
                    node = q.pop()
                    if node:
                        level.append(node.val)
                        q.appendleft(node.right)
                        q.appendleft(node.left)

                flag = False if flag else False
                if level:
                    res.append(level)

        return res
