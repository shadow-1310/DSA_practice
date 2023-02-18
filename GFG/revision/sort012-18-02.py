def sort012(arr:list[int], n:int) -> None:
    l = 0
    r = n - 1
    i = 0
    while l < r and i <=r:
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            i += 1
            l += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[r], arr[i] = arr[i], arr[r]
            r -= 1