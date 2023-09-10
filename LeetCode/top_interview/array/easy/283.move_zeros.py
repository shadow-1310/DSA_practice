#this is a wrong solution as it doesnot preserve orderof non zero elements
def move_zeros(nums):
    n = len(nums) 
    left = 0
    right = n - 1

    if n == 1:
        return nums
    else:
        while left < right:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1

        return nums


def move_zeros_new(nums):
    n = len(nums)
    i = 0
    count = 0
    while i < n:
        if nums[i]  == 0:
            nums.pop(i)
            count += 1
        else:
            i += 1
        
        n = len(nums)
    
    for i in range(count):
        nums.append(0)


#this is a revision done on 10-09-2023, but not working for all testcases in LC, one failed case is [0,1]
class Solution:
    def moveZeroes(self, nums):
        left = 0
        right = left

        while left <= right and right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            if nums[right] == 0:
                right += 1


#this is a revision done on 10-09-2023, working on all testcases of LC
class Solution:
    def moveZeroes(self, nums):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1

            else:
                i += 1

        for i in range(count):
            nums.append(0)

nums = [0,1,0,3,12]
nums1 = [0, 0, 1]
# print(move_zeros(nums))
move_zeros_new(nums1)
print(nums1)
