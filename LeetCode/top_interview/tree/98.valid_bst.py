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


#this is a revision done on 30-07-2023
#this is a wrong solution, think in terms of lowerr and upper bound for each node
class Solution:
    def isValidBST(self, root):
        def dfs(node, curr_lim):
            if not node or (not node.left and not node.right):
                return True

            if not node.left:
                left = True
            else:
                left_lim = min(curr_lim, node.left.val)
                if node.left.val >= curr_lim:
                    return False
                left = dfs(node.left, left_lim)

            if not node.right:
                right = True
            else:
                right_lim = max(curr_lim, node.right.val)
                if node.right.val <= curr_lim:
                    return False
                right = dfs(node.right, right_lim)

            return (left and right)

        if not root:
            return False
        return dfs(root, root.val)
            

class Solution:
    def isValidBST(self, root):
        def dfs(node, lb, ub):
            if not node:
                return True

            return node.val > lb and node.val < ub and dfs(node.left, lb, node.val) and dfs(node.right, node.val, ub)

        return dfs(root, float('-inf'), float('inf'))


#revision on 04-10-2023
class Solution:
    def isValidBST(self, root):
        def dfs(node, lb, ub):
            if not node:
                return True
            
            q_self = node.val < ub and node.val > lb
            q_left = dfs(node.left, lb, node.val) if node.left else True
            q_right = dfs(node.right, node.val, ub) if node.right else True

            return q_self and q_left and q_right

        return dfs(root, float('-inf'), float('inf'))

#revision done on 20-11-2023
class Solution:
    def isValidBST(self, root):
        def is_valid(node, ll, ul):
            if not node:
                return True
            curr_val = node.val
            
            q_self = curr_val < ul and curr_val > ll
            q_left = True if not node.left else is_valid(node.left, ll, curr_val)
            q_right = True if not node.right else is_valid(node.right, curr_val, ul)

            return q_left and q_right and q_self
        return is_valid(root, float('-inf'), float('inf'))
