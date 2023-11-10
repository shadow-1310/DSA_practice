from collections import defaultdict

class Solution:
    def numsSubarraysWithSum(self, nums, goal):
        l = 0
        res = 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > goal:
                curr -= nums[l]
                l += 1
            if curr == goal:
                res += 1

        return res

#I misunderstood the problem by thinking that I have to return the subsets rather than the count
# this solution returns the subsets but will not work on the testcases
#done on 10-11-2023
class Solution:
    def numsSubarraysWithSum(self, nums,goal):
        prefix_sum = defaultdict(list)
        prefix_sum[0].append(-1)
        curr = 0
        res = []
        for i,num in enumerate(nums):
            curr += num
            diff = curr - goal
            if diff in prefix_sum:
                for start in prefix_sum[diff]:
                    res.append(nums[start+1:i+1])
            prefix_sum[curr].append(i)

        return res
        

#this is the correct solution 
#done on 10-11-2023
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr = 0
        res = 0
        for num in nums:
            curr += num
            diff = curr - goal
            if diff in prefix_sum:
                res += prefix_sum[diff]

            prefix_sum[curr] += 1

        return res


s = Solution()
nums = [1,0,1,0,1]; goal = 2
print(s.numsSubarraysWithSum(nums, goal))
