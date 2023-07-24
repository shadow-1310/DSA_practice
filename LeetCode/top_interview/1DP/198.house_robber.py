class Solution:
    def rob(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            last = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = last

        return rob2

nums = [1,2,3,1]
s = Solution()
print(s.rob(nums))
