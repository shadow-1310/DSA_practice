from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i >= len(word):
                return True
            if (
                (r < 0 or c < 0) or 
                (r >= rows or c >= cols) or 
                ((r,c) in path) or 
                (board[r][c] != word[i])
                ):
                return False
            
            path.add((r,c))

            res = (
                (backtrack(r-1, c, i+1)) or
                (backtrack(r+1, c, i+1)) or
                (backtrack(r, c-1, i+1)) or
                (backtrack(r, c+1, i+1))
                )
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
                
        return False

#this is a revision done on 30-07-2023
class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, index):
            if index >= len(word):
                return True

            if r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in path or board[r][c] != word[index]:
                return False

            path.add((r,c))

            res = (dfs(r+1, c, index+1) or
                    dfs(r-1, c, index+1) or
                    dfs(r, c+1, index +1) or
                    dfs(r, c-1, index +1)
                    )
            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
