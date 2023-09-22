# this is a linear approach
def find_peak(nums):
    n =len(nums)
    
    if n == 1:
        return 0
    
    for i, num in enumerate(nums):
        if i == 0 and num > nums[1]:
            return i
        
        elif i == n-1 and num > nums[i-1]:
            return i 

        else:
            if (num > nums[i-1] and num > nums[i+1]):
                return i
            

# this is the optimized way with time complexity = O(logN)
def find_peak_binary(nums):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if mid == 0 and nums[mid] > nums[1]:
            return 0
        
        if mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
            return len(nums) - 1

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        else:
            if nums[mid+1] > nums[mid]:
                left = mid + 1
            elif nums[mid-1] > nums[mid]:
                right = mid - 1


#this is a revision done on 2023-09-22, Although it is working fine, the code becomes lengthy
class Solution:
    def findPeakElement(self, nums):
        left = 0
        n = len(nums) - 1
        if n == 0:
            return 0
        right = n

        while left <= right:
            mid = (left+right) // 2

            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                left = mid + 1

            elif mid == n:
                if nums[mid] > nums[mid-1]:
                    return mid
                right = mid - 1

            elif nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid

            elif nums[mid+1] > nums[mid]:
                left = mid + 1

            elif nums[mid-1] > nums[mid]:
                right = mid - 1


#this is copied from Neetcode youtube solution, it is working fine and short
#done on 2023-09-22
class Solution:
    def findPeakElement(self, nums):
        left = 0
        n = len(nums) - 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if mid > 0 and nums[mid-1] > nums[mid]:
                right = mid - 1

            elif mid < n and nums[mid] < nums[mid+1]:
                left = mid + 1

            else:
                return mid


nums = [1,2,1,3,5,6,4]
nums1 = [1,2,3,1]

print(find_peak_binary(nums))
print(find_peak_binary(nums1))
