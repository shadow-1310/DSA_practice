def brute(nums:list[int])-> int:
    n = len(nums)
    max_sum = nums[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum

def kaden(nums:list[int]):
    maxSub = nums[0]
    curr_sum = 0
    for n in nums:      
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n # this line is added after if condition. otherwise max will be 0 for -ve array
        maxSub = max(curr_sum, maxSub)
    return maxSub

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(brute(arr))
print(kaden(arr))
