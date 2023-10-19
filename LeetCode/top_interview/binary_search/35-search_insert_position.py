#revision done on 19-10-2023
class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1

        return l

s = Solution()
nums = [1,3,5,6]
target = 2
print(s.searchInsert(nums, target))
