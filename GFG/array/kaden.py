#brute force approach
def brute(arr:list[int])-> int:
    n = len(arr)
    max_sum = arr[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum

#optimized solution
def kaden(arr:list[int], N:int):
    maxSub = arr[0]
    curr_sum = 0
    for num in arr:      
        curr_sum += num # this line is added after if condition. otherwise max will be 0 for -ve array
        maxSub = max(curr_sum, maxSub)
        if curr_sum < 0:
            curr_sum = 0
    return maxSub

arr = [-2,1,-3,4,-1,2,1,-5,4]
N = 9
print(brute(arr))
print(kaden(arr, N))
