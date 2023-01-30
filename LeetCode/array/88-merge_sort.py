# merging with extra space
def merge(nums1:list, nums2:list, m:int, n:int) -> list:
    l = 0
    r = 0
    final = []
    while l < m and r < n:
        if nums1[l] <= nums2[r]:
            final.append(nums1[l])
            l += 1
        elif nums1[l] > nums2[r]:
            final.append(nums2[r])
            r += 1
    while l < m:
        final.append(a[l])
        l += 1
    while r < n:
        final.append(b[r])
        r += 1         

    return final


# merging without extra space (actual solution)
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