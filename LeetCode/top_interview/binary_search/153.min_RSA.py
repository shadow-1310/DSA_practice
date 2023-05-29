def find_mean(nums):
    left = 0
    right = len(nums)-1
    min_num = nums[0]

    while left < right:
        mid = (left+right) // 2
        min_num = min(min_num, nums[mid])

        if nums[mid] < nums[0]:
            right = mid - 1
            min_num = min(min_num, nums[right])
        
        elif nums[mid] >= nums[0]:
            left = mid + 1
            min_num = min(min_num, nums[left])    

    return min_num


nums = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

print(find_mean(nums))
print(find_mean(nums2))
print(find_mean(nums3))