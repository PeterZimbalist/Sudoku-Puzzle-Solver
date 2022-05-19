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