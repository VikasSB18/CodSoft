board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])

for turn in range(9):
    print_board()
    move = int(input("Enter position (0-8): "))
    board[move] = "X" if turn % 2 == 0 else "O"

print_board()
print("Game Over")
