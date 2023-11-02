class Solution:
    def numsSubarraysWithSum(self, nums, goal):
        l = 0
        res = 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > goal:
                curr -= nums[l]
                l += 1
            if curr == goal:
                res += 1

        return res


s = Solution()
nums = [1,0,1,0,1]; goal = 2
print(s.numsSubarraysWithSum(nums, goal))
