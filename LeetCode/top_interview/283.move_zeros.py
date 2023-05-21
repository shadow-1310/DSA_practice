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


nums = [0,1,0,3,12]
nums1 = [0, 0, 1]
# print(move_zeros(nums))
move_zeros_new(nums1)
print(nums1)