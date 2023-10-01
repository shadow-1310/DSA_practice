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
                

test1 = [["O","O","O"],["O","O","O"],["O","O","O"]]
s = Solution()
s.solve(test1)
print(test1)
