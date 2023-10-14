#done on 12-10-2023
class Solution:
    def findNumberOfLIS(self, nums):
        lis = {}
        max_lis, max_count = 0, 0
        
        for i in range(len(nums)-1, -1, -1):
            curr_lis, curr_count = 1, 1
            
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    l, c = lis[j]
                    if 1 + l > curr_lis:
                        curr_lis = 1 + l
                        curr_count = c
                    elif 1+l == curr_lis:
                        curr_count += c
            
            lis[i] = [curr_lis, curr_count]
            if curr_lis > max_lis:
                max_lis = curr_lis
                max_count = curr_count
            elif curr_lis == max_lis:
                max_count += curr_count
        
        return max_count

nums = [1,3,5,4,7]
s = Solution()
print(s.findNumberOfLIS(nums))
