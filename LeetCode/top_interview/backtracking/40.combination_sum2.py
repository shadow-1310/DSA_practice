from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if sum > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])

            backtrack(i+1, curr,sum + candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr, sum)

        backtrack(0, [], 0) 
        return res



#this ihs a revision done on 28-07-2023. but it is wrong, this algorithm doesn't use repeated numbers to calculate sum
# learning is we can't use for loop to backtrack, at every node we need to make 2 decisions only 
# then include all repeatitions in the left subtree but not in the right subtree
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(start, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return 

            if start >= len(candidates) or curr_sum > target:
                return 

            for i in range(start, len(candidates)):
                if i+1 < len(candidates) and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1, curr, curr_sum + candidates[i])
                curr.pop()

        dfs(0, [], 0)
        return res


#this is corrext revision done using 2 decision at each node approach
#done on 28-0-2023
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return 

            if curr_sum > target or i >= len(candidates):
                return 

            curr.append(candidates[i])
            dfs(start+1, curr, curr_sum + candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, curr, curr_sum)

        dfs(0, [], 0)
        return res


#this solution is wrong as it includes duplicate entry
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        def dfs(index, curr_sum, curr):
            if curr_sum == target:
                res.append(curr[:])
                return
            if curr_sum > target or index == len(candidates):
                return

            curr.append(candidates[index])
            dfs(index+1, curr_sum+candidates[index], curr)
            curr.pop()
            dfs(index+1, curr_sum, curr)

        dfs(0, 0, [])
        return res
    

#problem with this approach is it doesnot take duplicate entries for sum purpose, it is wrong
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        def dfs(start, curr_sum, curr):
            if curr_sum == target:
                res.append(curr[:])
                return
            if start == len(candidates) or curr_sum > target:
                return

            while start+1 < len(candidates) and candidates[start] == candidates[start+1]:
                start += 1
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(i+1, curr_sum+candidates[i], curr)
                curr.pop()

        candidates.sort()
        dfs(0, 0, [])
        return res

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(index, curr_sum, curr):
            if curr_sum == target:
                res.append(curr[:])
                return
            if index == len(candidates) or curr_sum > target:
                return

            curr.append(candidates[index])
            dfs(index+1, curr_sum+candidates[index], curr)
            curr.pop()
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, curr_sum, curr)

        dfs(0, 0, [])
        return res


s = Solution()
print(s.combin([10,1,2,7,6,1,5], 8))
