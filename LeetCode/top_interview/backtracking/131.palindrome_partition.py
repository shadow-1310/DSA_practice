from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(l, r):
            if l == r:
                return True
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            
            return True
        
        def backtrack(start, curr):
            if start >= len(s):
                res.append(curr.copy())
                return 
            
            for end in range(start, len(s)):
                str = s[start:end+1] 
                if is_palindrome(start, end):
                    curr.append(str)
                    backtrack(end+1 , curr)
                    curr.pop()

        backtrack(0, [])
        return res
    

# this is a revision done 29-07-2023
#correct solution
class Solution:
    def partition(self, s):
        res = []

        def is_palindrome(start, end):
            if start == end:
                return True

            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(start, curr):
            if start >= len(s):
                res.append(curr.copy())
                return 
            
            for end in range(start, len(s)):
                string = s[start:end+1]

                if is_palindrome(start, end):
                    curr.append(string)
                    dfs(end+1, curr)
                    curr.pop()

        dfs(0, [])
        return res

s = Solution()
print(s.partition('aab'))
