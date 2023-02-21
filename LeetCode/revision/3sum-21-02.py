def three_sum(nums:list[int]) -> list[list[int]]:
    result = []
    n = len(nums)
    nums.sort()
    print(nums)
    r = len(nums) - 1
    i = 0
    for i in range(n):
        if nums[i] == nums[i-1] and i!=0:
            continue
        l = i + 1
        r = n - 1
        while l < r and i < r:    
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return result

test = [-1,0,1,2,-1,-4]
print(three_sum(test))