import collections
class Solution:
    def numIslands(self, grid):
        islands = 0
        visited = set()
        row_lim = len(grid)
        col_lim = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                curr_row, curr_col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r = curr_row + dr
                    c = curr_col + dc
                    if ((r >= 0 and r < row_lim) and
                            (c >= 0 and c < col_lim) and
                            (r,c) not in visited and
                            grid[r][c] == '1'
                        ):
                        visited.add((r,c))
                        q.append((r,c))
        
        for r in range(row_lim):
            for c in range(col_lim):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)

        return islands

