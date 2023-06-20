# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this is correct solution using same_tree as a helper function
# done on 18-06-2023
class Solution:

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.is_same(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def is_same(self, p, q):
        if not p and not q:
            return True
        
        if (not p or not q):
            return False
        
        if (p.val != q.val):
            return False
        
        return (self.is_same(p.left, q.left) and self.is_same(p.right, q.right))
        