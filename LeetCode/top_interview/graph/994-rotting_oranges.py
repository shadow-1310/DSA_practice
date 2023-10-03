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

