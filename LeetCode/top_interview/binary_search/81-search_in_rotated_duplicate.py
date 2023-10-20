#done on 20-10-2023
class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid +1

            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
              
        return False

nums = [1,0,1,1,1]
target = 0
s = Solution()
print(s.search(nums, target))
