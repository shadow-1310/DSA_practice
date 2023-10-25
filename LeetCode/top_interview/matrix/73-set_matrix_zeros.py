class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        marks = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    marks.append([r,c])

        for r,c in marks:
            matrix[r] = [0]*cols
            for i in range(rows):
                matrix[i][c] = 0



s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix)
