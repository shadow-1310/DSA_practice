def two_sum(nums, target):
    diff_map = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in diff_map:
            return [diff_map[diff], index]
        else:
            diff_map[num] = index

#this is a revision done on 07-09-2023, working fine on LC testcases
class Solution:
    def twoSum(self, nums, target):
        diff = {}
        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]
            
            diff[target-num] = i


nums = [2, 7, 9,11]
target = 16
print(two_sum(nums, target))
