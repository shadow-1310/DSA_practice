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