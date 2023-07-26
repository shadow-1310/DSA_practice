from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        dp = set()
        dp.add(0)
        target = total // 2
        
        for i in range(len(nums)-1, -1, -1):
            temp_dp = set()

            for t in dp:
                if t+nums[i] == target :
                    return True
                temp_dp.add(t+nums[i])
                temp_dp.add(t)

            dp = temp_dp

        return True if target in dp else False

nums = [1,5,11,5]
s =Solution()
print(s.canPartition(nums))
