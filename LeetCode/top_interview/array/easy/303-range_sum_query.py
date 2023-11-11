class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0]*n
        self.prefix[0] = nums[0]
        for i in range(1, n):
            self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left, right):
        if left == 0:
            res = self.prefix[right]
        else:
            res = self.prefix[right] - self.prefix[left-1]

        return res

