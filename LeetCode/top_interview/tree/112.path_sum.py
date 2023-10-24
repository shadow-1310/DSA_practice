# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this is first approach and wrong solution
# done on 26-06-23
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
    
#this is correct solution using preorder DFS using recursive approach
# done on 29-06-23
class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        return dfs(root, 0)


#revision done on 24-10-2023
class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, curr):
            if curr > targetSum:
                return False
            if not node:
                return False
            if not node.left and not node.right and curr+node.val == targetSum:
                return True
            if dfs(node.left, curr+node.val) or dfs(node.right, curr+node.val):
                return True
            
            return False
        return dfs(root, 0)
