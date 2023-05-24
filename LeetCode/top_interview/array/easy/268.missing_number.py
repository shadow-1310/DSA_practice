def missing_num(nums):
    n = len(nums)
    required_sum = (n * (n+1)) // 2
    curr_sum = 0

    for num in nums:
        curr_sum += num

    missing = required_sum - curr_sum

    return missing

nums = [9,6,4,2,3,5,7,0,1]

print(missing_num(nums))