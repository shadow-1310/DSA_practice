# first done on 20-11-2023
class Solution:
    def constructMaximumBinaryTree(self, nums):
        def construct(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0], None, None)
            max_idx = 0
            max_val = 0
            i = 0
            for i, num in enumerate(arr):
                if num > max_val:
                    max_idx = i
                    max_val = num
            left = construct(arr[:max_idx])
            right = construct(arr[max_idx+1:])
            node = TreeNode(max_val, left, right)
            return node

        return construct(nums)
