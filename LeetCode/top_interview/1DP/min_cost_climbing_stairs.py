from typing import List

#this is a correct solution using Fibonnaci bottom up approach of DP with O(1) space complexity
# done on 18-07-2023
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last = cost[-1]
        penultimate = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            temp = penultimate
            penultimate = min(cost[i]+last, cost[i]+penultimate)
            last = temp

        return min(last, penultimate)
    

#this is also a correct solution overwriting the given array in bottomup approach. this solution is performing better on LeetCode
# done on 18-07-2023
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1,-1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])

s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

