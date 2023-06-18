# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this is a correct solution
# done on 18-06-2023
class Solution:
    def isSymmetric(self, root) -> bool:

        if not root:
            return True
        
        def is_same(p, q):
            if not p and not q:
                return True
            
            if (not p or not q) or (p.val != q.val):
                return False
            
            return (is_same(p.left, q.right) and is_same(p.right, q.left))
        
        return is_same(root.left, root.right)