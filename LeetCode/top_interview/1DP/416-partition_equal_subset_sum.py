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


#this is a revision done on 18-09-2023, working on LC testcases
class Solution:
    def canPartition(self,nums):
        tot = 0
        for n in nums:
            tot += n

        if tot % 2 != 0:
            return False

        tot = tot // 2

        sums = set()
        sums.add(0)

        for i in range(len(nums)-1, -1, -1):
            temp_sums = set()
            for j in sums:
                curr = nums[i] + j
                if curr == tot:
                    return True
                temp_sums.add(j)
                temp_sums.add(curr)

            sums = temp_sums

        return False


#revision done on 10-10-2023
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        if target & 1 != 0:
            return False
        else:
            target = target >> 1
        cache = {0}
        for i in nums:
            temp = set()
            for n in cache:
                res = i + n
                if res == target:
                    return True
                temp.add(res)
                temp.add(n)
            cache = temp

        return False


nums = [1,5,11,5]
# nums = [1,2,3,5]
s =Solution()
print(s.canPartition(nums))
