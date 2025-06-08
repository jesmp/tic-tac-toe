import random
import os

TTT = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


input_map = {
    'tl': (0, 0), 'tm': (0, 1), 'tr': (0, 2),
    'ml': (1, 0), 'mm': (1, 1), 'mr': (1, 2),
    'bl': (2, 0), 'bm': (2, 1), 'br': (2, 2),
}

# If run using cmd or terminal, screen will clear when method is called
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Makes robot pick their move while not picking a square the player has chosen
def robot_pick():
    empty = [(r, c) for r in range(3) for c in range(3) if TTT[r][c] == '-']
    if empty:
        r, c = random.choice(empty)
        TTT[r][c] = 'O'
    else:
        display_board()
        print("Game Over! No winners this time!")
        continue_game()

# Checks if someone has won
def check_for_win():
    for row in TTT:
        if all(cell == 'X' for cell in row):
            return True, 'X'
        elif all(cell == 'O' for cell in row):
            return True, 'O'

    # Checks columns
    for col in range(3):
        if all(TTT[row][col] == 'X' for row in range(3)):
            return True, 'X'
        elif all(TTT[row][col] == 'O' for row in range(3)):
            return True, 'O'

    # Checks main diagonal
    if all(TTT[i][i] == 'X' for i in range(3)):
        return True, 'X'
    elif all(TTT[i][i] == 'O' for i in range(3)):
        return True, 'O'

    # Checks anti-diagonal
    if all(TTT[i][2 - i] == 'X' for i in range(3)):
        return True, 'X'
    elif all(TTT[i][2 - i] == 'O' for i in range(3)):
        return True, 'O'

    return False, None

# Gets input from the user and adds their mark to the board
def get_player_move():
    while True:
        move = input("Choose a tile: tl, tm, tr, ml, mm, mr, bl, bm, br\n").strip().lower()
        if move in input_map:
            row, col = input_map[move]
            if TTT[row][col] == '-':
                TTT[row][col] = 'X'
                return
            else:
                print("Tile already taken.")
        else:
            print("Invalid input.")

# Displays board
def display_board():
    print("\n")
    for i in range(3):
        print("     |     |     ")
        print(f"  {TTT[i][0]}  |  {TTT[i][1]}  |  {TTT[i][2]}  ")
        print("     |     |     ")
        if i < 2:
            print("-----|-----|-----")
    print("\n")

# Starts the Game
def game_start():
    display_board()
    get_player_move()
    win, _ = check_for_win()
    if not win:
        robot_pick()

def reset_board():
    global TTT
    TTT = [['-', '-', '-'] for i in range(3)]

def continue_game():
    proceed = input("do you want to continue? type y or n\n").lower()
    if proceed == 'y':
        reset_board()
        game_on()
    else:
        pass

def game_on():
    while '-' in TTT[0] or '-' in TTT[1] or '-' in TTT[2]:
        clear_terminal()
        game_start()
        win, player = check_for_win()
        if win:
            clear_terminal()
            if player == 'X':
                display_board()
                print("Game over, You win!\n\n")
                continue_game()
                break
            else:
                clear_terminal()
                display_board()
                print("Game over, Computer wins!\n\n")
                continue_game()
                break

#test
if __name__ == '__main__':
    game_on()