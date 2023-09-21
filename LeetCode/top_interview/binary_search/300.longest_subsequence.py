# this is a dp problem so will attempt it later
# following code is half attempt only
def find_lis(nums):
    start = 0
    prev = start
    curr = prev + 1
    max_lis = 0
    count = 1

    if len(nums) == 1:
        return 1

    while prev < curr and curr < len(nums):
        if nums[start] > nums[start+1]:
            start += 1
            prev = curr
            curr = prev + 1
            count = 1
        
        elif nums[curr] > nums[prev]:
            count += 1
            curr += 1
            max_lis = max(max_lis, count)

        elif nums[right] :
            pass
        
        right += 1
# this is a correct solution with O(N^2) time complexity
# done on 25-07-2023
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        
        return max(lis)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))

# a solution with O(NlogN) time complexity, but tough
class Solution:
    def lengthOfLIS(self, nums):
        pass



#this is a revision done on 16-09-2023, working ok on LC
class Solution:
    def lengthOfLIS(self, nums):
        lis = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)
