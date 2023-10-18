from collections import deque

class Solution:
    def orangesRotting(self, grid):
        fresh = 0
        time = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (
                            (r < 0 or r == rows) or
                            (c < 0 or c == cols) or
                            grid[r][c] != 1
                        ):
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r,c))

            time += 1

        return time if fresh == 0 else -1


#revision done on 18-10-2023
class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1

        if not fresh:
            return 0
        #we are starting time from -1 because first loop is used in visitig the rotten oranges only
        time = -1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row,col) in visited:
                    continue
                visited.add((row,col))
                print(row,col)
                if grid[row][col] == 1:
                    fresh -= 1
                for dr, dc in dirs:
                    r = row+dr
                    c = col+dc
                    if (
                            (0 <= r < rows) and
                            (0<=c<cols) and 
                            (r,c) not in visited and 
                            grid[r][c] == 1
                        ):
                        q.append([r,c])
            print("------")
            time += 1

        return time if not fresh else -1
                

grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0]]
grid4 = [[2,2],[1,1],[0,0],[2,0]]
s = Solution()
print(s.orangesRotting(grid1))
print(s.orangesRotting(grid2))
print(s.orangesRotting(grid3))
print(s.orangesRotting(grid4))
