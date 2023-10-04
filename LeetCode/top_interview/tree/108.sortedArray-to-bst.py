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


class Solution:
    def sortedArrayToBST(self, nums):
        def bst(left, right):
            if left > right:
                return None

            mid = (left+right)//2
            node = TreeNode(nums[mid])

            node.left = bst(left, mid-1)
            node.right = bst(mid+1, right)

            return node

        return bst(0, len(nums)-1)


#revision on 04-10-2023, used bit manipulation to get mid element
class Solution:
    def sortedArrayToBST(self, nums):
        def dfs(l, r):
            if l > r:
                return None
            mid = (l+r) >> 1
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node

        return dfs(0, len(nums))
