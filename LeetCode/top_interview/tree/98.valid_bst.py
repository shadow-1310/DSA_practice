# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this is first attemp and wrong solution
# done on 20-06-2023
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        
        return ((root.left.val <= root.val if root.left else True) and (root.right.val >= root.val if root.right else True) and self.isValidBST(root.left) and self.isValidBST(root.right))
    
#this is second attempyt and correct solution
# done on 20-06-2023
class Solution:
    def isValidBST(self, root) -> bool:
        def is_valid(node, left, right):
            if not node:
                return True
            
            return node.val > left and node.val < right and is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)
        
        return is_valid(root, float('-inf'), float('inf'))