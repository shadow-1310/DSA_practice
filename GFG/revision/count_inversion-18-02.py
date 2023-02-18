def inversion(arr, n):
    count = 0
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        count += inversion(left, len(left))
        count += inversion(right, len(right))

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                count += 1
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return count

test = [3, 2, 4, 7, 6]
print(inversion(test, 5))