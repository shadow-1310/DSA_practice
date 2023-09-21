class Solution:
    def rob(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            last = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = last

        return rob2

#this is revision done on 2023-09-20, it is done using the bottom up approach
class Solution:
    def rob(self, nums):
        rob1 = 0
        rob2 = 0

        for i in range(len(nums)-1, -1, -1):
            curr = max(nums[i]+rob2, rob1)
            rob2 = rob1
            rob1 = curr

        return curr


nums = [1,2,3,1]
s = Solution()
print(s.rob(nums))
