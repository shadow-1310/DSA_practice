class Solution:
    def trap(self, height):
        n = len(height)
        left = [0]*n
        right = [0]*n
        res = 0
        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        for i in range(n):
            curr = height[i]
            boundary = min(left[i], right[i])
            if curr < boundary:
                res += boundary - curr

        return res

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
s = Solution()
print(s.trap(height1))
print(s.trap(height2))
