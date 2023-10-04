# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is first attempt on 11-06-2023
# this is correct solution with recurssive DFS approach
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

# this is second correct solution with iterative DFS
# done on 13--06-2023
class Solution:
    def maxDepth(self, root):
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth, res)
                stack.append([node.left, depth+1])
                stack.append([node.rigth, depth+1])
            
            return res

#this is a revision done on 30-07-2023
#tough to figure out the exact approach
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#this revision is done on 04-10-2023, although not efiicient as neetcode solution
class Solution:
    def maxDepth(self, root):
        def dfs(node, h):
            if not node:
                return h
            return max(dfs(node.left, h+1), dfs(node.right, h+1))
        return dfs(root,0)
