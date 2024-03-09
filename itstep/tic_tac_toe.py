import random

def show():
    for row in board:
        print(' '.join(row))

def winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

def player_move(difficulty):
    if player == "X":
        while True:
            try:
                row, col = map(int, input(f"{player} row and col (0 2): ").split())
                if board[row][col] == "-":
                    board[row][col] = player
                    return
                else:
                    print("position taken")
            except (ValueError, IndexError):
                print("Please, enter 2 numbers 0-2 separated by space")
    else:
        if difficulty == "easy":
            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if board[row][col] == "-":
                    print(f"Computer plays at row {row}, column {col}")
                    board[row][col] = player
                    return
                
        elif difficulty == "hard":
            opponent = "X" if player == "0" else "0"
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = opponent
                        if winner(opponent):
                            print(f"Computer plays at row {row}, column {col}")
                            board[row][col] = player
                            return
                        else:
                            board[row][col] = '-'
            
            strategic_positions = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]
            for row, col in strategic_positions:
                if board[row][col] == '-':
                    print(f"Computer plays at row {row}, column {col}")
                    board[row][col] = player
                    return

            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if board[row][col] == "-":
                    board[row][col] = player
                    return

board = [["-"] * 3 for _ in range(3)]
player = "X"
while True:
    level = input("Level (easy|hard): ")
    if level in ("easy", "hard"):
        break
    print("Invalid input")

while True:
    show()
    player_move(level)
    if winner(player):
        show()
        print(f"{player} wins")
        break
    player = "0" if player == "X" else "X"
    