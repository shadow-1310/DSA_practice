def contains_duplicate(nums):
    count_map = {}
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    for key in count_map:
        if count_map[key] > 1:
            return True
        
    return False


#revision done on 2023-11-23
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.containsDuplicate(nums))
# print(contains_duplicate(nums))
# print(check_duplicate(nums))
