def maxSubArray(nums:list[int]):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum <= 0:
                curr_sum = 0
    return max_sum

test = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(test))
            
