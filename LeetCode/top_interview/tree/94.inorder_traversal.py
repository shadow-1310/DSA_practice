# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#this is first attempt and corect solution with recurssive approach. done on 13-06-2023
# but solution is too long
class Solution:
    def inorderTraversal(self, root):
        node = root
        self.res = []
        if not root:
            return self.res
        else:
            self.traverse(root.left)
            self.res.append(root.val)
            self.traverse(root.right)
        
        return self.res
        
    def traverse(self, node):
        if node:
            if node.left:
                self.traverse(node.left)
                self.res.append(node.val)
                self.traverse(node.right)
            
            else:
                self.res.append(node.val)
                if node.right:
                    self.traverse(node.right)


# this is correct solution and more simplified version of recurssive call
# done on 13-06-2023
class Solution:
    def inorderTraversal(self, root):
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)

        return res


# this is correction solution with iteratiev approach
# done on 13-06-2023
class Solution:
    def inorderTraversal(self, root):
        stack = []
        res = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


#this is a revision
#done on 30-07-2023
class Solution:
    def inorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res


#revision done on 04-10-2023
class Solution:
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res
