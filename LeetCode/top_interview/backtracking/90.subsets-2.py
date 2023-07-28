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
    

#this is a revision done on 28-07-2023
#correct solution
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def dfs(index, curr):
            if index >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            dfs(index+1, curr)
            curr.pop()

            while index+1 <len(nums) and nums[index] == nums[index+1]:
                index += 1

            dfs(index+1, curr)

        dfs(0, [])
        return res
    
