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
            
s = Solution()
print(s.combine(4, 2))