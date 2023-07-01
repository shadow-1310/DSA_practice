# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is correct solution using recursive DFS(inorder traversal) approach
# done on 29-06-23
class Solution:
    def kthSmallest(self, root, k):
        if not root:
            return None
        res = []
        def dfs(node):
            if not node:
                return None
            
            if len(res) >= k:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k-1]
    
# this is a correct solution using iterative DFS 
# done on 29-06-2023
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val

            curr = curr.right 
            