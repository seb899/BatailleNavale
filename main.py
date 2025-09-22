from string import ascii_uppercase

BOARD_SIZE = 5
WATER = "~"

def make_board():
    return [[WATER for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    print("   " + " ".join(str(i+1) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        row_label = ascii_uppercase[i]
        row = " ".join(board[i])
        print(f"{row_label}  {row}")

def main():
    board = make_board()
    print("=== Bataille Navale ===")
    print_board(board)

if __name__ == "__main__":
    main()
