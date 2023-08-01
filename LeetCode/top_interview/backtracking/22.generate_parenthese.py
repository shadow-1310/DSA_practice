from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, curr):
            if open == close == n:
                res.append(''.join(curr))
                return
            
            if close > open :
                return           
            
            if open < n:
                curr.append('(')
                backtrack(open+1, close, curr)
                curr.pop()

            if close < open:
                curr.append(')')
                backtrack(open, close+1, curr)
                curr.pop()

        backtrack(0, 0, [])
        return res
    
#this is a revision. done on 29-07-2023
#correct solution more optimized than previous solution
class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(open, close, curr):
            if open == n and close == n:
                res.append("".join(curr))
                return

            if close > open or open > n or close > n:
                return
            
            curr.append("(")
            dfs(open+1, close, curr)
            curr.pop()
            curr.append(")")
            dfs(open, close+1, curr)
            curr.pop()

s = Solution()
print(s.generateParenthesis(3))

