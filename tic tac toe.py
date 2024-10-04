import math

# Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]  # 9 spaces for the 3x3 grid

# Function to print the current board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a winner
def winner(board, player):
    # Winning combinations: rows, columns, diagonals
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

# Function to check if the board is full (draw)
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    # Check for terminal states
    if winner(board, 'O'):
        return 1  # AI wins
    elif winner(board, 'X'):
        return -1  # Human wins
    elif is_board_full(board):
        return 0  # Draw

    # Maximizing player (AI's turn)
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score

    # Minimizing player (Human's turn)
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function to determine the AI's best move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to handle human move
def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            return int(move) - 1
        print("Invalid move, try again.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human move
        move = human_move()
        board[move] = 'X'
        print_board(board)

        if winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        move = ai_move(board)
        board[move] = 'O'
        print_board(board)

        if winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
