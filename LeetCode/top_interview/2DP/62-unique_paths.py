class Solution:
    def uniquePaths(self, m, n):
        cache = {}
        visited = set()
        def backtrack(r,c):
            if r == m or n == c:
                return 0
            if (r,c) in visited:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = backtrack(r+1,c) + backtrack(r, c+1)
            return cache[(r,c)]
    
        return backtrack(0,0)

s = Solution()
print(s.uniquePaths(3,2))
print(s.uniquePaths(3,7))

