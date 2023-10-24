#this is correct solution, it can be done without using defaultdict also
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        prev_sum = defaultdict(int)
        prev_sum[0] = 1
        res = 0
        
        curr_sum = 0
        for num in nums:
            curr_sum += num
            res += prev_sum[curr_sum - k]
            prev_sum[curr_sum] += 1

        return res


nums = [1,2,3]; k = 3
s = Solution()
print(s.subarraySum(nums,k))
