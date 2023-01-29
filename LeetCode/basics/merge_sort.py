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

a = [1, 2, 3]
b = [2, 5, 6]
m = 3
n = 3
print(merge(a, b, m, n))