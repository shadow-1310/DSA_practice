from typing import List

#this is a correct solution using backtracking
#done one 11-07-2023
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(curr_idx, subset):
            if curr_idx >= n:
                res.append(subset[::])
                return
            
            subset.append(nums[curr_idx])
            backtrack(curr_idx+1, subset)
            subset.pop()

            while curr_idx + 1 < n and nums[curr_idx] == nums[curr_idx+1]:
                curr_idx += 1

            backtrack(curr_idx + 1, subset)

        backtrack(0, [])
        return res