#done on 2023-09-24
class Solution:
    def jump(self,nums):
        res = 0
        l = 0
        r = l

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i+nums[i])

            l = r + 1
            r = far
            res += 1

        return res
