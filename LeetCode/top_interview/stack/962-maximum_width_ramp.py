#this approach is wrong as we need to find the farthest smaller number not nearest one
class Solution:
    def maxWidthRamp(self, nums):
        res = 0
        stack = []
        for i, num in enumerate(nums):
            while stack and num >= stack[-1][-1]:
                index, _ = stack.pop()
                res = max(res, i-index)
            stack.append([i,num])

        return res

#this solution is working but giving TLE, as it is not optimized
class Solution:
    def maxWidthRamp(self, nums):
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(n-1, i, -1):
                if nums[j] >= num:
                    res = max(res, j-i)
                    break
        return res

#optmized solution using monotonic stack
class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        n = len(nums)
        res = 0
        for i in range(n):
            if not stack or nums[i] <= nums[stack[-1]]:
                stack.append(i)

        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                index = stack.pop()
                res = max(res, i-index)
            stack.append(i)

        return res



nums = [6,0,8,2,1,5]
s = Solution()
print(s.maxWidthRamp(nums))
