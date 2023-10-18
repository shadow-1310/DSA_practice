from collections import deque
class Solution:
    def solve(self, board):
        us = set()
        rows = len(board)
        cols = len(board[0])
        #dfs to make all border 'O' regions to uncaptured
        def dfs(r, c):
            if (r,c) in us:
                return
            if ((r < 0 or c < 0) or
                    (r == rows or c == cols) or
                    board[r][c] != 'O'):
                    return
            us.add((r,c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        #calling the dfs only on the border cells
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    dfs(r,c)

        #calling the board and changing all cells which are not captured
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in us:
                    board[r][c] = 'X'
                

class Solution:
    def solve(self, board):
        visited = set()
        safe = set()
        rows = len(board)
        cols = len(board[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(r,c):
            if (r,c) in visited:
                return
            q = deque()
            q.append([r,c])
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if (r,c) in visited:
                        continue
                    visited.add((r,c))
                    for dr, dc in dirs:
                        row = r+dr
                        col = c+dc
                        if (
                            row >= 0 and col >= 0 and
                            row < rows and col < cols and
                            (row,col) not in visited and board[row][col] == 'O'
                            ):
                                safe.add((row,col))
                                q.append([row,col])

        #check first and last col for safe 'O'
        for i in range(rows):
            for j in [0,cols-1]:
                if board[i][j] == 'O' and (i,j) not in visited:
                    safe.add((i,j))
                    bfs(i,j)

        #check first and last row for safe 'O'
        for i in [0,rows-1]:
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    safe.add((i,j))
                    bfs(i,j)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in safe:
                    board[r][c] = 'X'




test1 = [["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]]

board = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
s = Solution()
s.solve(test1)
s.solve(board)
print(test1)
print(board)
