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


#this is a revision done on 07-09-2023, working ok on LC testcases
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1

            else:
                count[num] = 1

        bucket_list = [[] for i in range(len(nums)+1)]
        for key in count:
            bucket_list[count[key]].append(key)

        for i in range(len(bucket_list)-1, -1, -1):
            if len(bucket_list[i]) != 0:
                for num in bucket_list[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res


#this revision was done on 14-10-2023
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        if k > len(nums):
            return res

        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        bucket_list = [ [] for i in range(len(nums)+1)]
        for key in count_map:
            bucket_list[count_map[key]].append(key)

        for i in range(len(bucket_list)-1, -1, -1):
            for num in bucket_list[i]:
                res.append(num)
                if len(res) == k:
                    return res


#revision done on 2023-11-23
class Solution:
    def topKFrequent(self, nums, k):
        dict = {}
        max_freq = 0
        res = []
        n = len(nums)
        if k > n:
            return res
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            max_freq = max(max_freq, dict[num])

        freq_map = [[]] * (max_freq+1)
        for key in dict:
            if freq_map[dict[key]]:
                freq_map[dict[key]].append(key)
            else:
                freq_map[dict[key]] = [key]

        count = 0
        for i in range(len(freq_map)-1, 0, -1):
            num = freq_map[i]
            for n in freq_map[i]:
                res.append(n)
                count += 1
                if count == k:
                    return res

nums = [1,1,1,2,2,3]
k = 2

nums2 = [1]
k2 = 1

nums3 = [-1, -1]
k3 = 1


s = Solution()
print(s.topKFrequent(nums, k))
print(s.topKFrequent(nums2, k2))
print(s.topKFrequent(nums3, k3))
