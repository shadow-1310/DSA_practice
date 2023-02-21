def missing(nums:list[int]):
    n = len(nums)
    sum = 0
    req_sum = (n * (n+1)) // 2
    for num in nums:
        sum += num
    missing_num = req_sum - sum 
    return missing_num

test = [9,6,4,2,3,5,7,0,1]
print(missing(test))