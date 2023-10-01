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

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid2 = [[0,0,0,0,0,0,0,0]]
# print(grid)
s = Solution()
print(s.maxAreaOfIsland(grid))
print(s.maxAreaOfIsland(grid2))


