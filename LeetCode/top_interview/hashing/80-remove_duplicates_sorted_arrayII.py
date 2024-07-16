#this is first done on 21-11-2023, not the most optimized solution
from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums):
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        idx = 0
        for key in count_map:
            if count_map[key] >= 2:
                nums[idx] = key
                idx += 1
                nums[idx] = key
                idx += 1

            else:
                nums[idx] = key
                idx += 1

        return idx

nums = [0,0,1,1,1,1,2,3,3]
s = Solution()
print(s.removeDuplicates(nums))
