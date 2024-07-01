def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = '.'  # Backtrack

    return False

def n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

# Example usage:
n_queens(4)