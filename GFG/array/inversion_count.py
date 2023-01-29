def brute(arr:list, n:list):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

a = [2, 4, 1, 3, 5]
n = 5
print(brute(a, n))