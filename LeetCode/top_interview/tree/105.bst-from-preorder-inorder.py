# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is correct solution
# done on 20-06-2023
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        mid = inorder.index(preorder[0])
        node = TreeNode(preorder[0])

        node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return node