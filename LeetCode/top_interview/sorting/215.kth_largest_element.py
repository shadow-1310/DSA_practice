# this is the first attempt on 01-06-2023
# this is the correct solution and passes Leetcode tescases
# it is using quicksort algorithm with Hoare partitioning scheme, (Neetcode uses Lomuto scheme which I found difficult)

def find_kth_largest(nums, k):
    if len(nums) == 1:
        return nums[0]   

    def quicksort(arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right]

        while i < j:
            while i < right and arr[i] < pivot:
                i += 1
            
            while j > left and arr[j] >= pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

        # i is the partitioning position here
        if i == desired:
            return arr[i]

        elif i < desired:
            return quicksort(arr, i + 1, right)
        
        else:
            return quicksort(arr, left, i - 1)                  
            
    left = 0
    right = len(nums) - 1
    desired = len(nums) - k
    
    return quicksort(nums, left, right)


nums = [3,2,1,5,6,4]
k = 2

nums2 = [3,2,3,1,2,4,5,5,6]
k2= 4

nums3 = [1]
k3 = 1

nums4 = [2, 1]
k4 = 1

print(find_kth_largest(nums, k))
print(find_kth_largest(nums2, k2))
print(find_kth_largest(nums3, k3))
print(find_kth_largest(nums4, k4))