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
        

nums = [1,2,1,3,5,6,4]
nums1 = [1,2,3,1]

print(find_peak_binary(nums))
print(find_peak_binary(nums1))