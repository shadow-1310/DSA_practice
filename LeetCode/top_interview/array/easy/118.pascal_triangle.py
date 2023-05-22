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


rows = 7
print(pascal_triangle(rows))