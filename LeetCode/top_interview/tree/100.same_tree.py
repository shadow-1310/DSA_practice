# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


#this is a revision done on 31-07-2023
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#revision done on 04-10-2023
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        q_self = (p.val == q.val)
        q_left = self.isSameTree(p.left, q.left)
        q_right = self.isSameTree(p.right, q.right)

        return q_self and q_left and q_right
            
