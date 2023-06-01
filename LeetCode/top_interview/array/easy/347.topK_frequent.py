#this is first attempt and it is wrong. It works for the basic test_cases but doesnot work for all
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


# this is revision - 1,  done on 01-06-2023. this is the correct solution
def top_frequent(nums, k):
    freq_map = {}

    if len(nums) == 1:
        return [nums[0]]

    # generating the freq count of elements in nums
    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    #initializing the empty bucket list
    bucket_list = [[] for _ in range(len(nums) + 1)]
    print(freq_map)
    print(bucket_list)

    # iterating through the freq_map and filling the bucket list
    for key in freq_map:
        index = freq_map[key]
        bucket_list[index].append(key)
    
    res = []

    #finally going through the bucket list in reverse order to fill the 'res' list
    for i in range(len(nums), -1, -1):
        if len(bucket_list[i]) != 0:
            for ele in bucket_list[i]:
                res.append(ele)

        if len(res) == k:
            return res
        


nums = [1,1,1,2,2,3]
k = 2

nums2 = [1]
k2 = 1

nums3 = [-1, -1]
k3 = 1


print(top_frequent(nums, k))
print(top_frequent(nums2, k2))
print(top_frequent(nums3, k3))