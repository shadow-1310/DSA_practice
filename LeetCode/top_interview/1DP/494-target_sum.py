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


#done on 09-10-2023, but doesn't pass test cases diue to time constraint
#this is a backtrack solution without using DP approach
class Solution:
    def findTargetSumWays(self, nums, target):
        def backtrack(index, curr):
            if index == len(nums) :
                if curr == target:
                    return 1
                return 0
            res = 0
            res += backtrack(index+1, curr + nums[index])
            res += backtrack(index+1, curr - nums[index])

            return res
        return backtrack(0, 0)


class Solution:
    def findTargetSumWays(self, nums, target):
        cache = {}
        def backtrack(index, curr):
            if index == len(nums):
                if curr == target:
                    return 1
                return 0
            if (index, curr) in cache:
                return cache[(index, curr)]

            cache[(index, curr)] = (
                                    backtrack(index+1, curr+nums[index])
                                    + backtrack(index+1, curr-nums[index])
                                    )
            return cache[(index, curr)]
        return backtrack(0,0)



s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))
print(s.findTargetSumWays([1], 1))
