def brute(arr:list, n:int, k:int) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            sum = arr[i] + arr[j]
            if sum == k:
                count += 1
    return count

def count_pair(arr:list, n:int, k:int) -> int:
    count = 0
    prev = {}
    for i, num in enumerate(arr):
        if num in prev:
            prev[num] += 1
        else:
            prev[num] = 1
    for num in arr:
        diff = k - num
        if diff in prev:
            count += prev[diff]
            if k - num == num:
                count -= 1
    return count // 2

n = 4
k = 2
a = [1, 1, 1, 1]
print(brute(a, n, k))
print(count_pair(a, n, k))