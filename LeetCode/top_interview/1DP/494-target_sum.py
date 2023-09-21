# this is a first attempt done on 2023-09-20, working on LC testcases
class Solution:
    def findTargetSumWays(self, nums, target):
        cache = {}

        def backtrack(index, t):
            if index == len(nums):
                return 1 if t == target else 0

            if (index, t) in cache:
                return cache[(index, t)]

            cache[(index, t)] = (backtrack(index+1, t + nums[index]) + 
                                backtrack(index+1, t - nums[index]))

            return cache[(index, t)]

        return backtrack(0, 0)

