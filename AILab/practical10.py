N = 8

# Function to print solution
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))


# Function to check safe position
def is_safe(board, row, col):

    # Check left side row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


# Backtracking function
def solve(board, col):

    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):

            board[i][col] = 1

            if solve(board, col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False


# Main program
board = [[0]*N for _ in range(N)]

if solve(board, 0):
    print("Solution for 8-Queens Problem:\n")
    print_board(board)
else:
    print("No solution found")
