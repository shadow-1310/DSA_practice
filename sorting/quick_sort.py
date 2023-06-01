def quick_sort(arr, left, right):
    def partition(arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right]

        while i < j:
            while i < right and arr[i] < pivot:
                i += 1

            while j > left and arr[j] >= pivot:
                j -= 1
            
            if i <= j: 
                arr[i], arr[j] = arr[j], arr[i]

        if arr[i] > pivot and i != j:
            arr[i], arr[right] = arr[right], arr[i]

        return i

    if left < right:    
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos+1 , right)


nums = [11, 22, 77, 44, 5, 3, 2, 88]
nums2 = [2,1]
print(nums)
quick_sort(nums, 0, 7)
quick_sort(nums2, 0, 1)
print(nums)
print(nums2)