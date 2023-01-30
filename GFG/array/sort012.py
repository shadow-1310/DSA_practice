#brute force method using extra space
def brute(arr:list, n:int)->list:
    l = 0
    r = n -1
    c = 0
    result = [0 for i in range(n)]
    while c < n :
        if arr[c] == 0:
            result[l] = arr[c]
            l += 1
        elif arr[c] == 2:
            result[r] = arr[c]
            r -= 1
        else:
            result[c] = arr[c]
        c += 1
    return result

test = [0, 2, 1, 2, 0]
n = 5
brute(test, n)
print(brute(test, n))

def sort012(arr:list, n:int) -> None:
    l = 0
    r = n-1
    c = 0
    while c <= r:
        if arr[c] == 0:
            arr[l], arr[c] = arr[c], arr[l]
            l += 1
            c += 1
        elif arr[c] == 2:
            arr[r], arr[c] = arr[c], arr[r]
            r -= 1
        else:
            c += 1

print(test)
sort012(test, n)
print(test)