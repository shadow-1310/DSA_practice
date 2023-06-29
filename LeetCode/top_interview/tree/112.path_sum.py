# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        
        def dfs(node, curr_sum, target):
            if not node:
                return False
            
            curr_sum += node.val

            if curr_sum == target and (not node.right or not node.left):
                return True 
            
            return dfs(node.left, curr_sum, target) or dfs(node.right, curr_sum, target)
        
        return dfs(root, 0, targetSum)