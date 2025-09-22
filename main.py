from string import ascii_uppercase
import random
BOARD_SIZE = 5
WATER = "~"
SHIP_SIZE = 3
SHIP = "S"
HIT = "X"
MISS = "o"

def make_board():
    return [[WATER for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    print("   " + " ".join(str(i+1) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        row_label = ascii_uppercase[i]
        row = " ".join(board[i])
        print(f"{row_label}  {row}")

def place_ship(board):
    direction = random.choice(["H", "V"])
    placed = False
    while not placed:
        if direction == "H":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - SHIP_SIZE)
            for i in range(SHIP_SIZE):
                board[row][col+i] = SHIP
            placed = True
        else:
            row = random.randint(0, BOARD_SIZE - SHIP_SIZE)
            col = random.randint(0, BOARD_SIZE - 1)
            if all(board[row+i][col] == WATER for i in range(SHIP_SIZE)):
                for i in range(SHIP_SIZE):
                    board[row+i][col] = SHIP
                placed = True

def take_shot(board, hidden, row, col):
    if board[row][col] == SHIP:
        hidden[row][col] = HIT
        board[row][col] = HIT
    else:
        hidden[row][col] = MISS

def main():
    board = make_board()
    for _ in range(3):
        place_ship(board)

    hidden_board = make_board()

    print("=== Bataille Navale ===")
    print("Grille avant tir :")
    print_board(hidden_board)

    # Tir de test en A1 (0,0)
    take_shot(board, hidden_board, 0, 0)

    print("\nAprès un tir en A1 :")
    print_board(hidden_board)
if __name__ == "__main__":
    main()