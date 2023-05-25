def search_2d(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    r = 0
    c = cols - 1

    while r < rows and c < cols:
        value = matrix[r][c]

        if target > value:
            r += 1
        elif target < value:
            c -= 1
        else:
            return True
        
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 28

print(search_2d(matrix, target))