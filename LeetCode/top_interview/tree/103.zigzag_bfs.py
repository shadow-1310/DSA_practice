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


#this is a revision done on 01-08-2023
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)
        left  = True
        while q:
            level = []

            for i in range(len(q)):

               if left:
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

            if level:
                res.append(level)
                    
            left = ~left
        return res



#revision done on 04-10-2023, got wasted time in debugging, 
#the error was we can't reverse a boolean using ~, we have to use 'not' in front
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        q = deque()
        q.append(root)
        dir_left = True

        while q:
            level = []
            for i in range(len(q)):
                if dir_left:
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

            dir_left = not dir_left
            if level:
                res.append(level)

        return res
