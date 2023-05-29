def topK_freq(nums, k):
    count_map = {}
    res = []
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    
    bucket_list = [[] for i in range(len(nums))]

    for key in count_map:
        index = count_map[key]
        bucket_list[index].append(key)
    
    i = len(nums) - 1
    count = 0

    while True:
        res.extend(bucket_list[i])
        i -= 1
        if len(res) == k:
            return res

nums = [1,1,1,2,2,3]
k = 2

nums2 = [1]
k2 = 1

print(topK_freq(nums, k))
print(topK_freq(nums2, k2))