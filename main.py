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
    if hidden[row][col] != WATER:
        print(" Tu as déjà tiré ici, choisis une autre case.")
        return False

    if board[row][col] == SHIP:
        hidden[row][col] = HIT
        board[row][col] = HIT
        print("Touché !")
    else:
        hidden[row][col] = MISS
        print("À l'eau...")


    return True
def parse_input(move):
    row = ascii_uppercase.index(move[0].upper())
    col = int(move[1]) - 1
    return row, col

def all_ships_sunk(board):
    for row in board:
        if SHIP in row:
            return False
    return True
def has_won(board):
    for row in board:
        if SHIP in row:
            return False
    return True

    
def main():
    board = make_board()
    for _ in range(3):
        place_ship(board)

    hidden_board = make_board()
    shots = 0
    max_shots = 15   

    print("=== Bataille Navale ===")

    while True:
        print_board(hidden_board)
        move = input(f"Entrez une case (ex: A1, ou q pour quitter) [{shots}/{max_shots}]: ")

        if move.lower() == "q":
            print(f"Partie terminée après {shots} tirs.")
            break

        row, col = parse_input(move)

        if take_shot(board, hidden_board, row, col):
            shots += 1

            if all_ships_sunk(board):
                print_board(hidden_board)
                print(f" Bravo, tu as coulé tous les bateaux en {shots} tirs !")
                break

            if shots >= max_shots:
                print(" Tu as utilisé tous tes tirs... Partie perdue !")
                break

if __name__ == "__main__":
    main()
