def serach(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows - 1

    while left <= right:
        mid = (left+right) // 2

        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            right = mid - 1
        else:
            left = mid + 1

    target_row = right
    left = 0
    right = cols - 1

    while left <= right:
        mid = (left+right) // 2

        if matrix[target_row][mid] == target:
            return True
        elif matrix[target_row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [[1,2,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3

print(serach(matrix, target))
# print(len(matrix))