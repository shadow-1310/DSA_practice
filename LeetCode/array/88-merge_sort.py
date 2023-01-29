def merge_sort(nums1:list[int], m:int, nums2:list[int], n: int):
    i = m + n - 1 # index for final sorted array

    #merging in reverse
    while m > 0 and n > 0 :
        if nums1[m-1] > nums2[n-1]:
            nums1[i] = nums1[m-1]
            m -= 1
        else:
            nums1[i] = nums2[n-1]
            n -= 1
        i -= 1
        
    #filling nums1 with leftover nums2 elements
    while n > 0:
        nums1[i] = nums2[n-1]
        n -= 1
        i -= 1
    

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge_sort(nums1, m, nums2, n)
print(nums1)