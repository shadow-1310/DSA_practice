class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s) : 1}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i+1)

            if (i+1 < len(s)) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                res += dfs(i+2)

            cache[i] = res
            return res
        return dfs(0)


s = Solution()
print(s.numDecodings('226'))
