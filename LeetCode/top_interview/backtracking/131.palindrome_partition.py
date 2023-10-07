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

#this approach is not working, I don't know why
class Solution:
    def partition(self, s):
        res = []
        tot = len(s)
        def is_palindrome(l, r):
            # print(s[l:r+1])
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(start, end, curr):
            if not is_palindrome(start, end):
                return

            curr.append(s[start:end+1])
            if end == tot-1:
                res.append(curr.copy())
                return
            for i in range(end+1, tot):
                dfs(end+1, i, curr)
            curr.pop()

        for i in range(tot):
            dfs(0, i, [])
        return res

#revision on 06-10-2023
class Solution:
    def partition(self, s):
        res = []
        n = len(s)
        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start,curr):
            if start >= n:
                res.append(curr[:])
                return
            for i in range(start, n):
                if is_palindrome(start, i):
                    curr.append(s[start:i+1])
                    dfs(i+1, curr)
                    curr.pop()

        dfs(0, [])
        return res

s = Solution()
print(s.partition('aab'))
print(s.partition('abba'))

