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
        

nums = [1,2,1,3,5,6,4]
nums1 = [1,2,3,1]

print(find_peak(nums))
print(find_peak(nums1))