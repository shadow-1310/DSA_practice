def brute(nums:list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


#this is a revision done on 12-09-2023, working on all LC testcases
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

test = [-2,1,-3,4,-1,2,1,-5,4]
print(brute(test))
