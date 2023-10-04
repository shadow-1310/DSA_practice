# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        res = []
        def preorder(root):
            if not root:
                return
            res.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return res


#this is a revision
#done on 30-07-2023
class Solution:
    def preorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res


#this revision done on 04-0-2023
class Solution:
    def preorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
