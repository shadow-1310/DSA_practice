class Solution:
    def solveNQueens(self, n):
        cols = set()
        posd = set()
        negd = set()
        board = [ ['.']*n for i in range(n)]
        res = []

        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or r+c in negd or r-c in posd:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                posd.add(r-c)
                negd.add(r+c)
                dfs(r+1)
                board[r][c] = '.'
                cols.remove(c)
                posd.remove(r-c)
                negd.remove(r+c)

        dfs(0)
        return res


s = Solution()
print(s.solveNQueens(4))
# print(s.solveNQueens(8))
