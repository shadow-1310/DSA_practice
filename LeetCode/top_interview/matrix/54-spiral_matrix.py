#this solution is not working on singlwe row or single column and not correct solution
class Solution:
    def spiralOrder(self, matrix):
        l = 0
        r = len(matrix[0]) - 1
        top = 0
        bot = len(matrix) - 1 
        res = []

        while top <= bot and l <= r:
            for i in range(l, r):
                res.append(matrix[top][i])
            for i in range(top, bot):
                res.append(matrix[i][r])
            for i in range(r, l, -1):
                res.append(matrix[bot][i])
            for i in range(bot, top, -1):
                res.append(matrix[i][l])

            if l==r and top==bot:
                res.append(matrix[top][l])

            l += 1
            r -= 1
            top += 1
            bot -= 1
        return res


#this is the correct solution
#done on 25-10-2023
class Solution:
    def spiralOrder(self, matrix):
        l = 0
        r = len(matrix[0]) 
        top = 0
        bot = len(matrix) 
        res = []

        while top < bot and l < r: 
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot):
                res.append(matrix[i][r-1])
            r -= 1

            #this is the line tricky to get, it is added for single column or single row matrix case, which is in example 3 here
            if not (l < r and top < bot):
                break

            for i in range(r-1, l-1, -1):
                res.append(matrix[bot-1][i])
            bot -= 1

            for i in range(bot - 1, top-1, -1):
                res.append(matrix[i][l])
            l += 1

        return res

s = Solution()
matrix1 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = [[6,9,7]]
print(s.spiralOrder(matrix1))
print(s.spiralOrder(matrix2))
print(s.spiralOrder(matrix3))
