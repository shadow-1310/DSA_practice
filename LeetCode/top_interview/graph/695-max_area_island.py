from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid):
        visited = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        rows = len(grid)
        cols = len(grid[0])
        all_areas = []
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            area = 1
            visited.add((r,c))
            while q:
                curr_row, curr_col = q.popleft()
                for dr, dc in directions:
                    r = curr_row + dr
                    c = curr_col + dc
                    if (
                            (r >= 0 and c >= 0) and 
                            (r < rows and c < cols) and 
                            grid[r][c] == 1 and 
                            (r,c) not in visited
                        ):
                        visited.add((r,c))
                        area += 1
                        q.append((r,c))

            all_areas.append(area)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    bfs(r,c)

        return max(all_areas) if all_areas else 0


#revised on 18-10-2023
class Solution:
    def maxAreaOfIsland(self, grid):
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            curr = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    if (row,col) in visited:
                        continue
                    visited.add((row,col))
                    curr += 1
                    for dr,dc in dirs:
                        r = row+dr
                        c = col+dc
                        if (
                            r < rows and c < cols and
                            r >= 0 and c >= 0 and 
                            (r,c) not in visited and 
                            grid[r][c] == 1
                            ):
                            q.append([r,c])
            return curr

        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    res = max(res, bfs(r,c))

        return res




grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid2 = [[0,0,0,0,0,0,0,0]]

grid3 = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
# print(grid)
s = Solution()
# print(s.maxAreaOfIsland(grid1))
# print(s.maxAreaOfIsland(grid2))
print(s.maxAreaOfIsland(grid3))


