def single_number(nums):
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    for key in count_map:
        if count_map[key] == 1:
            return key


#this is a revision done on 10-09-2023, woeking on LC testcases
class Solution:
    def singleNumber(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1

            else:
                count[num] = 1

        for key in count:
            if count[key] == 1:
                return key

#this solutio is done on 2023-09-30
#it uses O(1) space unlike above
class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num

        return res


class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n

        return res

#revision done on 2023-11-23
class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
nums = [4,1,2,1,2]
print(single_number(nums))
