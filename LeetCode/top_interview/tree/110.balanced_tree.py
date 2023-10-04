# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = ((left[0] and right[0]) and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


#this is a revision done on 31-07-2023
#correct solution
class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            balanced = (left[0] and right[0]) and (abs(left[1]-right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return [True, 0]
            q_left = dfs(node.left)
            q_right = dfs(node.right)
            q_self = (q_left[0] and q_right[0]) and (abs(q_left[1] - q_right[1]) <= 1)
            h = 1 + max(q_left[1], q_right[1])

            return [q_self, h]

        return dfs(root)[0]
