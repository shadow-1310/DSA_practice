#this is a wrong approach
class Solution:
    def findChampion(self, grid):
        res = set()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    strong = r
                    weak = c
                    if weak in res:
                        res.remove(weak)
                    res.add(strong)
        return list(res).pop()


#this is a correct solution, done on 05-11-2023
class Solution:
    def findChampion(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            if sum(grid[r]) == cols - 1:
                return r


s = Solution()
grid1 = [[0,0,1],[1,0,1],[0,0,0]]
grid2 = [[0,1],[0,0]]
print(s.findChampion(grid1))
print(s.findChampion(grid2))

