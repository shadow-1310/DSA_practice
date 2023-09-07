def missing_num(nums):
    n = len(nums)
    required_sum = (n * (n+1)) // 2
    curr_sum = 0

    for num in nums:
        curr_sum += num

    missing = required_sum - curr_sum

    return missing

#this is a revision done on 07-09-2023, working fine on LC
class Solution:
    def missingNumber(self, nums):
        tot = len(nums)
        req_sum = (tot * (tot+1)) // 2
        given_sum = 0
        for n in nums:
            given_sum += n

        return req_sum - given_sum

nums = [9,6,4,2,3,5,7,0,1]

print(missing_num(nums))
