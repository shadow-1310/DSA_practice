# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# this is first approach and coorect solution , the code can be shortened
# done on 20-06-2023
class Solution:
    def mergeTrees(self, root1, root2):
        def merge(p, q):
            if not p and not q:
                return 
            
            v1 = p.val if p else 0
            v2 = q.val if q else 0
            v = v1 + v2
            node = TreeNode(v)

            if p and q:            
                node.left = merge(p.left, q.left)
                node.right = merge(p.right, q.right)
            
            elif p and not q:
                node.left = merge(p.left, None)
                node.right = merge(p.right, None)

            else:
                node.left = merge(None, q.left)
                node.right = merge(None, q.right)
            
            return node
        
        return merge(root1, root2)


# this is second approach with the code shortened 
# correct solution done on 20-06-2023
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return node
