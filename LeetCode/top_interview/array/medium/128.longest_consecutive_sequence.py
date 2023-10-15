# this is first attempt on 01-06-2023
def find_longest(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    check_list = set(nums)
    max_count = 0
    for num in nums:
        if num - 1 not in check_list:
            count = 1
            while True:
                if num + 1 in check_list:
                    count += 1 
                    max_count = max(count, max_count)
                    num += 1
                else:
                    break

    return max(max_count, count)


#this is a revision done on 08-09-2023, working better than previous solutions on LC
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        max_range = 0
        for num in nums:
            if num-1 not in nums:
                curr = num
                curr_range = 0
                while curr in nums:
                    curr_range += 1
                    curr += 1

                max_range = max(max_range, curr_range)

        return max_range


#although this is working find, it is taking longer time to execute in LC compared to previous approaches
#revision done on 14-10-2023
class Solution:
    def longestConsecutive(self, nums):
        check = set(nums)
        res = 0
        for num in nums:
            curr = 0
            if num-1 not in check:
                while num in check:
                    curr += 1
                    num += 1
                res = max(res, curr)
        return res



nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [0]
nums4 = []

print(find_longest(nums1))
print(find_longest(nums2))
print(find_longest(nums3))
print(find_longest(nums4))
