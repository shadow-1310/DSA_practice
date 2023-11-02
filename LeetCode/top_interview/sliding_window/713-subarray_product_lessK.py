#this is done on 01-11-2023
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        res = 0
        curr = 1
        l = 0
        for r in range(n):
            curr *= nums[r]
            while curr >= k and l <= r:
                curr = curr // nums[l]
                l += 1

            res += r-l+1

        return res


nums = [10,5,2,6]; k = 100
s = Solution()
print(s.numSubarrayProductLessThanK(nums,k))
