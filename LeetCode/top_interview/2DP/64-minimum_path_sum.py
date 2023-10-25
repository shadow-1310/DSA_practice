class Solution:
    def minPathSum(self, grid):
        INF = float('inf')
        rows = len(grid)
        cols = len(grid[0])
        cache = [ [0]*(cols+1) for i in range(rows+1)]
        for i in range(cols+1):
            cache[rows][i] = INF

        for i in range(rows+1):
            cache[i][cols] = INF
        cache[rows][cols-1] = 0

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                cache[r][c] =  grid[r][c] + min(cache[r+1][c], cache[r][c+1])

        return cache[0][0]


grid = [[1,3,1],[1,5,1],[4,2,1]]
s  = Solution()
print(s.minPathSum(grid))

