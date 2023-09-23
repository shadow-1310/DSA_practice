# it is done on 2023-09-23
#this is a greedy approach with O(N) time complexity
class Solution:
    def canJump(self,nums):
        target = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return True if target == 0 else False
