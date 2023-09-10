# this is a naive incompleted approach
def valid_sudoku(board):
    #checking each row for duplicate entry
    for row in board:
        count_row = {}
        for ele in row:
            if ele  == '.':
                continue
            
            else:
                if ele not in count_row and (int(ele) < 10 and int(ele) > 0): # checking if the element already occured or it is in between 0-9
                    count_row[ele] = 1
                else:
                    return False
                
    for i in range(9):
        count_column = {}
        for row in board:
            ele = row[i]
            if ele == '.':
                continue
            else:
                if ele not in count_column and (int(ele) < 10 and int(ele) > 0): # checking for duplicate and valid entry in column wise
                    count_column[ele] = 1
                else:
                    return False
             
    return True


#this is the final soution
def is_valid_sudoku(board):
    '''
    we will initialize three sets of hashmaps one for each row, column and 3x3 squares
    '''
    rows = [{} for _ in range(9)]
    columns = [{} for _ in range(9)]
    squares = [[{} for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            ele = board[r][c]

            if ele == '.':
                continue
            
            #checking if the element in the range 0-9
            if int(ele) < 0 or int(ele) > 9:
                return False
            
            else:
                if ((ele in rows[r]) or (ele in columns[c]) or (ele in squares[r//3][c//3])):
                    return False
                    
                else:
                    rows[r][ele] = 1
                    columns[c][ele] = 1
                    squares[r//3][c//3][ele] = 1

    return True

# this is a revision. done on 11-06-2023
# although it is passing the testcases. the main approach should be initialize hashmaps not lists and check also if 0<val<9
def is_valid(board):
    cols = [[] for i in range(9)]
    rows = [[] for i in range(9)]
    squares = [[[] for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]

            if val == ".":
                continue

            else:
                if val in rows[i]:
                    return False
                else:
                    rows[i].append(val)

                if val in cols[j]:
                    return False
                else:
                    cols[j].append(val)

                if val in squares[i//3][j//3]:
                    return False
                else:
                    squares[i//3][j//3].append(val)

    return True


#this is a revision done on 10-09-2023, working on LC testcases
#this approach doesnot use an extra space to check duplicate value instead uses the original board
class Solution:
    def isValidSudoku(self, board):
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                ele = board[i][j]
                if ele == ".":
                    continue

                if int(ele) < 1 or int(ele) > 9:
                    return False
                
                #checking the same row
                for col in range(len(board[i])):
                    if board[i][col] == ele and col != j:
                        return False

                #checking the same column
                for row in range(rows):
                    if ele == board[row][j] and row != i:
                        return False
                
                #checking the 3*3 box
                row_min = (i // 3) * 3
                row_max = row_min + 3
                col_min = (j // 3) * 3
                col_max = col_min + 3

                for row in range(row_min, row_max):
                    for col in range(col_min, col_max):
                        if ele == board[row][col] and i != row and j != col:
                            return False

        return True


board =  [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,["6","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))
print(is_valid(board))
