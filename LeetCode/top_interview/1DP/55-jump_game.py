from typing import List

class Solution:
    def canJump(self, nums: List[int] -> bool:
        cache = [False]*(len(nums)-1)
        def dfs(index):
            if index == (len(nums) - 1):
                return True
            if index >= len(nums) or cache[index] == False:
                return False

            jump = nums[index]
            for i in range(1, jump+1):
                dfs(index+i)
            
                
