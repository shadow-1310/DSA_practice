from typing import List

#this is correct soluton using hashmap for determining if num is already in permutation
#done on 11-07-2023
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(curr, count):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            if len(curr) > n:
                return
            
            for i in range(n):
                if nums[i] not in count:
                    curr.append(nums[i])
                    count[nums[i]] = 1
                    backtrack(curr, count)
                    curr.pop()
                    count.pop(nums[i])

        backtrack([], {})
        return res

#this is 2nd approach, instead of using hashmap to count, we are boolean array here
#correct solution done on 11-07-2023
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False]*n
        def backtrack(curr, count):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            if len(curr) > n:
                return
            
            for i in range(n):
                if not used[i]:
                    curr.append(nums[i])
                    used[i] = True
                    backtrack(curr, used)
                    curr.pop()
                    used[i] = False

        backtrack([], used)
        return res

# this is a revision done on 26-07-2023

class Solution:
    def permute(self, nums):
        res = []
        used = [False for i in range(len(nums)+1)]

        def dfs(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            if len(curr) > len(nums):
                return

            for j in range(len(nums):
                if not used[j]: 
                    curr.append(nums[j])
                    used[j] = True
                    dfs(curr, used)
                    used[j] = False
                    curr.pop()

        dfs([], used)
        return res


s = Solution()
arr = [1,2,3]
arr2 = [1]
arr3 = [0,1]

print(s.permute(arr))
print(s.permute(arr2))
print(s.permute(arr3))
