def sort_colors(nums:list[int]) -> list[int]:
    l = 0
    r = len(nums) - 1
    i = 0
    while l < r and i <= r :
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            i += 1
            l += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
    return nums


#this is a revision done on 10-09-2023, working fine with LC testcases
class Solution:
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        curr = left

        while left < right and curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1

            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1

            else:
                curr += 1

test = [2,0,2,1,1,0]
print(sort_colors(test))
