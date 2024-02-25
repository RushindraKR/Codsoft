import math
X = 'X'
O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('----------')

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def evaluate(board):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for move in possible_moves(board):
            board[move[0]][move[1]] = X
            eval = minimax(board, depth+1, alpha, beta, False)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in possible_moves(board):
            board[move[0]][move[1]] = O
            eval = minimax(board, depth+1, alpha, beta, True)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in possible_moves(board):
        board[move[0]][move[1]] = X
        eval = minimax(board, 0, alpha, beta, False)
        board[move[0]][move[1]] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move
def play_game():
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are O and the AI is X.")
    print_board(board)
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != EMPTY:
            print("That cell is already occupied. Please choose another one.")
            continue
        board[row][col] = O
        print_board(board)
        if check_winner(board, O):
            print("Congratulations! You win!")
            break
        elif board_full(board):
            print("It's a tie!")
            break
        print("AI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = X
        print_board(board)
        if check_winner(board, X):
            print("AI wins! Better luck next time.")
            break
        elif board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
