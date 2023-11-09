def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--|---|--")

def check_win(board, player):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if all(board[cell // 3][cell % 3] == player for cell in win):
            return True
    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    print("Welcome to Tic Tac Toe")

    while True:
        print_board(board)
        print(f"{player}'s Chance")
        value = int(input("Please enter a value (0-8): "))

        if value < 0 or value > 8 or board[value // 3][value % 3] != ' ':
            print("Invalid input. Try again.")
            continue

        board[value // 3][value % 3] = player

        if check_win(board, player):
            print_board(board)
            print(f"{player} Won the match")
            break

        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
