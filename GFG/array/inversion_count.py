# brute force approach using 2 loops
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

# optimized solution using merge sort
def merge_sort(arr:list):
    count_inv = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        count_inv += merge_sort(left_arr)
        count_inv += merge_sort(right_arr)

        i = 0 # idx of left_arr
        j = 0 # idx for right_arr
        k = 0 # idx for sorted arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                count_inv += len(left_arr) - i
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return count_inv

test1 = [10, 10, 10]
test2 = [2, 4, 1, 3, 5]
print("test case1 before sorting: ",test1)
print("inversion count: ",merge_sort(test1))
print("test case 1 after sorting: ",test1)
print("\n")
print("test case2 before sorting: ",test2)
print("inversion count: ",merge_sort(test2))
print("test case 2 after sorting: ",test2)