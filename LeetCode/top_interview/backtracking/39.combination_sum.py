from typing import List

#correct solution done with recursive approach where no duplicates are allowed
#done on 11-07-2023
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or sum > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, sum + candidates[i])

            curr.pop()
            dfs(i+1, curr, sum)

        dfs(0, [], 0)
        
        return res


# this is a revision done on 26-07-2023
# and surprisingly this solution is faster in letcode evaluation
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(start, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if start >= len(candidates) or curr_sum > target:
                return 

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(i, curr,curr_sum+candidates[i])
                curr.pop()

        dfs(0, [], 0)
        return res


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        if len(candidates) == 0:
            return res

        def dfs(index, curr_sum, curr):
            if curr_sum == target:
                res.append(curr[:])
                return
            if index == len(candidates) or curr_sum > target:
                return

            curr.append(candidates[index])
            dfs(index, curr_sum+candidates[index], curr)
            curr.pop()
            dfs(index+1, curr_sum, curr)

        dfs(0, 0, [])
        return res

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
