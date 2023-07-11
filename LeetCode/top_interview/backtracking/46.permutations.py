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


s = Solution()
arr = [1,2,3]
arr2 = [1]
arr3 = [0,1]

print(s.permute(arr))
print(s.permute(arr2))
print(s.permute(arr3))