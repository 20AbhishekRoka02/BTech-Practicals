# Function to print the board
def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

# Function to check winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True

    return False


# Main Program
board = [" " for i in range(9)]
current_player = "X"

for turn in range(9):

    print_board(board)

    position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = current_player
    else:
        print("Position already filled! Try again.")
        continue

    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} Wins!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

else:
    print_board(board)
    print("Match Draw!")

