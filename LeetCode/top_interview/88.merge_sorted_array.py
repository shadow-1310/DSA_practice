def merge_sorted(nums1, m, nums2, n):
    p1 = m -1
    p2 = n - 1
    p3 = m +n - 1
    while p1 >=0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p3] = nums2[p2]
            p2 -= 1
        else:
            nums1[p3] = nums1[p1]
            p1 -= 1
        p3 -= 1
    
    while p1 >= 0:
        nums1[p3] = nums1[p1]
        p1 -= 1
        p3 -= 1
    
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge_sorted(nums1, m, nums2, n)
print(nums1)