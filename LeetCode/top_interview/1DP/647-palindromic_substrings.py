class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


class Solution:
    def countSubstrings(self, s):
        count = 0

        for i in range(len(s)):
            count += 1
            left = i - 1
            right = i + 1
            while i >= 0  and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    count += 1
                    left -= 1
                    right += 1

        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    count += 1
                    left -= 1
                    right += 1

        return count


#this revision was done on 11-10-2023
class Solution:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0  and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

        return count


#this revision done on 21-11-2023
class Solution:
    def countSubstrings(self, s):
        res = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1

            l = i
            r = i+1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1

        return res

s = Solution()
print(s.countSubstrings('abc'))
print(s.countSubstrings('aaa'))
print(s.countSubstrings('fdsklf'))
