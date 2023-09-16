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

s = Solution()
print(s.countSubstrings('abc'))
