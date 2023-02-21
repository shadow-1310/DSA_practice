def kadane(arr, N):
    max_sum = arr[0]
    curr_sum = 0
    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

test = (1,2,3,-2,5)
print(kadane(test, 5))