# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# this is correct solution done on 22-06-2023
# mistake was I was comparing with the root value instead compare to the curr value
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                return curr