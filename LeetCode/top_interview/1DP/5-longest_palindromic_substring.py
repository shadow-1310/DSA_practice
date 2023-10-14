class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0

        for i in range(len(s)):
            #for odd len strings
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l +1 > max_len:
                    res = s[l:r+1]
                    max_len = r-l+1

                l -= 1
                r += 1

                
                
            # for even len string
            l = i
            r = i+1
            while l>= 0 and r< len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    res = s[l:r+1]
                    max_len = r-l+1

                l -= 1
                r += 1

        return res 


#this is a revision done on 16-09-2023, working on all LC testcases
class Solution:
    def longestPalindrome(self, s):
        res = s[0]
        curr = 0
        max_count = 0

        for i in range(len(s)):
            left = i - 1
            right = i + 1
            curr = 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break

                else:
                    curr += 2
                    max_count = max(curr, max_count)
                    if curr == max_count:
                        res = s[left: right + 1]
                    left -= 1
                    right += 1

        for i in range(len(s)):
            left = i
            right = i + 1
            curr = 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break

                else:
                    curr += 2
                    max_count = max(curr, max_count)
                    if curr == max_count:
                        res = s[left: right + 1]
                    left -= 1
                    right += 1
        
        return res


#this revision was done on 11-10-2023
class Solution:
    def longestPalindrome(self, s):
        max_string = 0
        res = ''
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_string:
                    max_string = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_string:
                    res = s[l:r+1]
                    max_string = r-l+1
                l -= 1
                r += 1

        return res
            

s = Solution()
s2 = "cbbd"
print(s.longestPalindrome('babad'))
print(s.longestPalindrome(s2))
