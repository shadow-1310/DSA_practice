# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#this is my first approach. it is correct solution done on 11-06-2023
# problem is no need to use extra function
class Solution:
    def invertTree(self, root):
        def invert(node):
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp

                if node.left:
                    invert(node.left)

                if node.right:
                    invert(node.right)
        
        node = root
        invert(node)

        return root
    

# this is updated version on 11-06-2023
# this is correct
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


#this is a revision done on 31-07-2023
#correct solution
class Solution:
    def invertTree(self, root):
        def make_invert(node):
            if not node:
                return

            temp = node.left
            node.left = node.right
            node.right = temp
            
            make_invert(node.left)
            make_invert(node.right)

        make_invert(root)
        return root



class Solution:
    def invertTree(self, root):
        def dfs(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
