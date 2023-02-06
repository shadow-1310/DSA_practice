def missing(nums:list[int])->int:
    n = len(nums)
    req_sum = (n*(n+1))//2
    sum = 0
    for num in nums:
        sum += num
    missing_num = req_sum - sum
    return missing_num

test = [9,6,4,2,3,5,7,0,1]
print(missing(test))