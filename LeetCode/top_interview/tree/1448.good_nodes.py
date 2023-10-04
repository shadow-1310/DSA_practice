# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):        
        def dfs(node, max_val):
            if not node:
                return 0
            
            res = 1 if node.val >= max_val else 0
            max_val = max(node.val, max_val)

            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            return res
        
        return dfs(root, root.val)


#I have used a different approach using global variable
#learn the other method also
#revision done on 04-0-2023
class Solution:
    def goodNodes(self, root):
        global count
        count = 0
        def dfs(node, curr_max):
            global count
            if not node:
                return
            if node.val > curr_max:
                count += 1
                curr_max = node.val

            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, 0)
        return count
