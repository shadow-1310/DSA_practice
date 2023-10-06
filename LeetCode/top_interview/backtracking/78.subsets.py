from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


# this is a revision
class Solution:
    def subsets(self, nums):
        res = []

        def dfs(index, curr):
            if index >= len(nums):
                res.append(curr.copy())
                return res

            curr.append(nums[index])
            dfs(index+1, curr)
            curr.pop()
            dfs(index+1, curr)

        dfs(0, [])
        return res


class Solution:
    def subsets(self, nums):
        res = []
        def dfs(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return

            dfs(index+1, curr)
            curr.append(nums[index])
            dfs(index+1, curr)
            curr.pop()

        dfs(0, [])
        return res


s = Solution()
print(s.subsets([1,5,7,3]))

