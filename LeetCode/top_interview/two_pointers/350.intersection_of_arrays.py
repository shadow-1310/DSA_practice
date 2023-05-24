def intersection(nums1, nums2):
    '''
    it is an wrong approach.. I kept it because of remembering my wrong approach
    '''
    i = 0
    j = 0
    result = []
    while i < len(nums1):
        j = 0
        while j < len(nums2) and i < len(nums1):
            if nums1[i]  == nums2[j]:
                result.append(nums1[i])
                nums1.pop(i)
                nums2.pop(j)
            else:
                j += 1
        i += 1

    return result

# from collections import Counter
def intersection2(nums1, nums2):
    '''
    in this approach we are making our own counter dictionary rather than using collections.counter()
    '''
    counter = {}
    result = []
    
    for num in nums1:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    for num in nums2:
        if num in counter:
            result.append(num)
            counter[num] -= 1
        else:
            continue

    return result


nums1 = [1, 2]
nums2 = [2, 1, 3]
print(intersection2(nums1, nums2))
