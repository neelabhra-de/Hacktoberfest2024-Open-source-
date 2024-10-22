# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to play Tic-Tac-Toe
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # X always goes first

    # Game loop
    while True:
        print_board(board)

        # Get the current player's move
        print(f"Player {current_player}'s turn:")
        row, col = map(int, input("Enter row and column numbers (1-3) separated by a space: ").split())
        row -= 1  # Convert to 0-indexed
        col -= 1  # Convert to 0-indexed

        # Check if the move is valid
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue

        # Place the player's marker
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
