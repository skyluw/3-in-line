def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def check_winner(board, player):
    # Combinaciones ganadoras
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(spot != ' ' for spot in board)

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        move = int(input(f"Jugador {current_player}, ingresa tu movimiento (1-9): ")) - 1

        if board[move] != ' ':
            print("Este lugar ya está ocupado. Intenta de nuevo.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Felicidades! El jugador {current_player} ha ganado.")
            break

        if is_board_full(board):
            print_board(board)
            print("Es un empate.")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
