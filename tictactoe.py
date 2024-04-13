import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False, alpha, beta)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already taken. Please choose an empty cell.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid row and column.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        print("Your turn (X)")
        row, col = player_move(board)
        board[row][col] = human
        print_board(board)

        if check_winner(board, human):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI's turn (O)")
        row, col = get_best_move(board)
        board[row][col] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
