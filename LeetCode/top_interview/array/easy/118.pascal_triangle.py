def pascal_triangle(numRows):
    triangle = []
    for row in range(numRows):
        row_nums = []
        for i in range(row+1):
            if i == 0:
                row_nums.append(1)
            elif i == row:
                row_nums.append(1)
            else:
                value = triangle[row-1][i] + triangle[row-1][i-1]
                row_nums.append(value)
        
        triangle.append(row_nums)

    return triangle


#this is a revision done on 10-09-2023, working on all testcases of LC
class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)

                else:
                    if i > 0:
                        row.append(res[i-1][j-1] + res[i-1][j])

            res.append(row)

        return res


class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            level = []
            for j in range(i+1):
                if j == 0 or j == i:
                    level.append(1)

                else:
                    level.append(res[i-1][j-1] + res[i-1][j])
            res.append(level)

        return res


#revision done on 2023-11-23
class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            rows = i+1
            curr = []
            for r in range(rows):
                if r == 0 or r == i:
                    curr.append(1)
                else:
                    curr.append(res[-1][r-1] + res[-1][r])
            res.append(curr)

        return res


rows = 7
print(pascal_triangle(rows))
