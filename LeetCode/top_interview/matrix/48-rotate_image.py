#done on 25-10-2023
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        l = 0
        r = n-1
        while l < r:
            for i in range(r-l):
                top = l
                bot = r
                
                temp = matrix[top][l+i]
                matrix[top][l+i] = matrix[bot-i][l]
                matrix[bot-i][l] = matrix[bot][r-i]
                matrix[bot][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp

            l += 1
            r -= 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)
