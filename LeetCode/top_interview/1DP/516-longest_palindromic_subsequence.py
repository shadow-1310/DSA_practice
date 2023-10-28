class Solution:
    def longestPalindromeSubseq(self, s):
        cache = [ [0]*(len(s)+1) for i in range(len(s)+1) ]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if s[i] == s[len(s)-j-1]:
                    cache[i][j] = 1 + cache[i+1][j+1]
                else:
                    cache[i][j] = max(cache[i+1][j], cache[i][j+1])

        return cache[0][0]


#revision done on 27-10-2023
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        cache = [ [0] * (n+1) for i in range(n+1) ]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[n-j-1]:
                    cache[i][j] = 1 + cache[i+1][j+1]
                else:
                    cache[i][j] = max(cache[i][j+1], cache[i+1][j])

        return cache[0][0]



s = Solution()
print(s.longestPalindromeSubseq('bbab'))
print(s.longestPalindromeSubseq('cbbd'))

