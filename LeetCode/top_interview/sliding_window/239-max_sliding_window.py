from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        l = 0
        r = 0
        q = deque()
        res = []
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)
            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res


nums1 = [1,3,-1,-3,5,3,6,7]; k1 = 3
nums2 = [1]; k2 = 1
nums3 = [7,2,4]; k3 = 2
s = Solution()
print(s.maxSlidingWindow(nums1, k1))
print(s.maxSlidingWindow(nums2, k2))
print(s.maxSlidingWindow(nums3, k3))
