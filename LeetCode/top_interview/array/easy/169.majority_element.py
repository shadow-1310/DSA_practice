def majority(nums):
    n = len(nums)
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    for key in count_map:
        if count_map[key] > n/2:
            return key


#this is a revision done on 10-09-2023
#it is done using Moore's voting algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        res = nums[0]
        for num in nums:
            if count == 0:
                res = num
                count += 1

            elif num == res:
                count += 1

            elif num != res:
                count -= 1

        if count != 0:
            count = 0
            for num in nums:
                if num == res:
                    count += 1

        if count > len(nums) / 2:
            return res
        
nums = [2,2,1,1,1,2,2]
print(majority(nums))
