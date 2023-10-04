# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        res = []

        def postorder(root):
            if not root:
                return
            
            postorder(root.right)
            postorder(root.left)
            res.append(root.val)

        postorder(root)

        return res


#it is a revision done on 30-07-2023
class Solution:
    def postorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


class Solution:
    def postorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
