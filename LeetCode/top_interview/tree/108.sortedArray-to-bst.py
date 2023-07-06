# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is a correct solution 
# done on 20-06-2023
class Solution:
    def sortedArrayToBST(self, nums):
        def make_tree(l, r):
            if l > r:
                return None
            
            mid = (l+r) // 2
            node = TreeNode(nums[mid])
            node.left = make_tree(l, mid-1)
            node.right = make_tree(mid+1, r)

            return node
        
        return make_tree(0,len(nums)-1)