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
    
s = Solution()
print(s.generateParenthesis(3))