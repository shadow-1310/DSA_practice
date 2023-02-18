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

test = [2,0,2,1,1,0]
print(sort_colors(test))