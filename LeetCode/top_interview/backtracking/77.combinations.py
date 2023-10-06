from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if len(curr) > k or start > n:
                return 
                       
            for j in range(start, n+1):
                curr.append(j)
                dfs(j+1, curr)
                curr.pop()
        
        dfs(1, [])
        return res
            
# s = Solution()
# print(s.combine(4, 2))


#this is a revision done on 26-07-2023
class Solution:
    def combine(self, n, k):
        res = []
        subset = []
        def dfs(start, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            if start > n:
                return 

            for i in range(start+1, n+1):
                dfs(i, subset.append(i))
        
        dfs(0, [])
        return 


#although this solution is correct, it is less efificnet no need to maintain the record of visited nodes
class Solution:
    def combine(self, n, k):
        res = []
        visited = set()

        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr[:])
            if start > n:
                return

            for i in range(start, n+1):
                if i not in visited:
                    visited.add(i)
                    curr.append(i)
                    dfs(i+1, curr)
                    visited.remove(i)
                    curr.pop()

        dfs(1, [])
        return res
    

#this is a revision done on 06-10-2023
class Solution:
    def combine(self, n, k):
        res = []

        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr[:])
            if start > n:
                return

            for i in range(start, n+1):
                curr.append(i)
                dfs(i+1, curr)
                curr.pop()

        dfs(1, [])
        return res



s = Solution()
print(s.combine(5, 3))
