def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        l = i+1
        r = n - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while l < r :
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return result

arr = [0,0,0]
print(three_sum(arr))