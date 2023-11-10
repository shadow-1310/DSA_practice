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


#revision done on 10-11-2023
class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = defaultdict(lambda:0)
        prefix_sum[0] = 1
        curr = 0
        res = 0
        for num in nums:
            curr += num
            diff = curr - k
            if diff in prefix_sum:
                res += prefix_sum[diff]
            prefix_sum[curr] += 1

        return res


nums = [1,2,3]; k = 3
s = Solution()
print(s.subarraySum(nums,k))
