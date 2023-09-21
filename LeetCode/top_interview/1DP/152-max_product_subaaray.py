from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = 1
        curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue
            
            temp = curr_max * n
            curr_max = max(curr_max*n, curr_min*n, n)
            curr_min = min(temp, curr_min*n, n)
            
            res = max(curr_max, res)

        return res

# this is a revision done on 2023-09-20, working on LC testcases
class Solution:
    def maxProduct(self, nums):
        curr_max = 1
        curr_min = 1
        max_single = nums[0]
        max_nums = max_single

        for n in nums:
            max_single = max(max_single, n)
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue
        
            temp = max_nums * n
            curr_max = max(curr_max*n, curr_min*n, n)
            curr_min = min(curr_min*n, temp, n)

            max_nums = max(max_nums, curr_max)

        return max(max_single, max_nums)
        


nums = [2,3,-2,4]
s = Solution()
print(s.maxProduct(nums))
