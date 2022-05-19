<<<<<<< HEAD
board = [
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [0, 7, 0, 3, 0, 0, 0, 1, 2]
]

def solve(bo):
    find = find_blanks(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
           
            bo[row][col] = 0
        
    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_blanks(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
   
    return None


solve(board)

print_board(board)
=======
def find_empty_position(board):
    #scan each row and column for empty positions
    #an empty position is indicated by -1

    for row in range(9):
        for col in range(9):
            if board[row][col] == -1:
                return row, col

    return None, None   #if there are no empty positions


def is_valid(board, guess, row, col):
    #evaluates whether the guess matches any other number in the row, column, or 3x3 box
    #returns True if valid and False if not

    #checks the row
    row_values = board[row]
    if guess in row_values:
        return False

    #checks the column
    col_values = [board[i][col] for i in range(9)]
    if guess in col_values:
        return False

    #checks the 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False

    return True


def sudoku_solver(board):

    row, col = find_empty_position(board)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess 

            if sudoku_solver(board):
                return True

        board[row][col] = -1    #reset guess if is_valid is False

    return False    #return False if there is no valid guess for any position


if __name__ == '__main__':
    board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(sudoku_solver(board))
    print(board)
>>>>>>> 9060b50c1f4fc0f7cdcc3225d07f82d9d696cb4c
