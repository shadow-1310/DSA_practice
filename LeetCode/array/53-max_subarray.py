def brute(nums:list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

test = [-2,1,-3,4,-1,2,1,-5,4]
print(brute(test))