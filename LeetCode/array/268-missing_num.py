def missing_num(nums: list[int]) -> int:
    n = len(nums)
    req_sum = int(n*(n+1) / 2)
    sum = 0
    for num in nums:
        sum += num
    missing = req_sum - sum
    return missing


input = [3, 0, 1]
print(missing_num(input))
