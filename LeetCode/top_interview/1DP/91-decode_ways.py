class Solution:
    def numDecodings(self, s: str) -> int:
        cache = set()
        for i in range(1, 27):
            cache.add(i)

        def dfs(start):
            if start >= len(s):
                return 

