import random
import os
import time

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def switch_player(p):
    return 'O' if p == 'X' else 'X'

def colored(c):
    if c == 'X': return RED + 'X' + RESET
    if c == 'O': return BLUE + 'O' + RESET
    return ' '

def check_win(board, size, p):
    for r in range(size):
        if all(board[r*size + c] == p for c in range(size)): return True
    for c in range(size):
        if all(board[r*size + c] == p for r in range(size)): return True
    if all(board[i*size + i] == p for i in range(size)): return True
    if all(board[i*size + (size-i-1)] == p for i in range(size)): return True
    return False

def board_full(board):
    return all(c != ' ' for c in board)

def ai_easy(board):
    return random.choice([i for i, c in enumerate(board) if c == ' '])

def ai_hard(board, size, ai, human):
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = ai
            if check_win(board, size, ai):
                board[i] = ' '
                return i
            board[i] = ' '
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = human
            if check_win(board, size, human):
                board[i] = ' '
                return i
            board[i] = ' '
    return ai_easy(board)

def draw_board(board, size):
    for r in range(size):
        for c in range(size):
            i = r*size + c
            print(colored(board[i]) if board[i] != ' ' else f"{i+1}", end='')
            if c < size-1: print(" | ", end='')
        print()

WIN_LINES = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def new_ultimate():
    return [[' ']*9 for _ in range(9)], [' ']*9

def small_win(ub, b, p):
    return any(all(ub[b][i] == p for i in line) for line in WIN_LINES)

def big_win(bb, p):
    return any(all(bb[i] == p for i in line) for line in WIN_LINES)

def ultimate_ai_easy(ub, bb):
    boards = [i for i in range(9) if bb[i] == ' ']
    b = random.choice(boards)
    cells = [i for i, c in enumerate(ub[b]) if c == ' ']
    return b, random.choice(cells)

def ultimate_ai_hard(ub, bb, ai, human):
    for b in range(9):
        if bb[b] == ' ':
            for c in range(9):
                if ub[b][c] == ' ':
                    ub[b][c] = ai
                    if small_win(ub, b, ai):
                        ub[b][c] = ' '
                        return b, c
                    ub[b][c] = ' '
    for b in range(9):
        if bb[b] == ' ':
            for c in range(9):
                if ub[b][c] == ' ':
                    ub[b][c] = human
                    if small_win(ub, b, human):
                        ub[b][c] = ' '
                        return b, c
                    ub[b][c] = ' '
    return ultimate_ai_easy(ub, bb)

def show_ultimate(ub):
    for br in range(3):
        for r in range(3):
            for bc in range(3):
                b = br*3 + bc
                for c in range(3):
                    i = r*3 + c
                    print(colored(ub[b][i]) if ub[b][i] != ' ' else f"{i+1}", end='')
                    if c < 2: print('|', end='')
                if bc < 2: print(" | | ", end='')
            print()
        if br < 2: print("==========================")

def main():
    random.seed()
    clear()
    print("Welcome to S56 companies")
    print("\nTic Tac Toe: Ultimate Legends.")

    game = int(input("Choose Game type:\n1. 3x3\n2. 4x4\n3. 5x5\n4. Ultimate\nEnter the number of Game you want: "))
    mode = int(input("\nChoose Game mode:\n1. Player vs Player\n2. Player vs AI\nEnter the number of the mode you want: "))

    vs_ai = mode == 2
    ai_level = None

    if vs_ai:
        p1 = input("\nLet Bonk AI know your name!\nEnter your name: ")
        p2 = "Bonk AI"
        ai_level = int(input("\nAI Level:\n1. Easy\n2. Hard\nEnter the number of AI level you want: "))
    else:
        p1 = input("Enter Player 1 name: ")
        p2 = input("Enter Player 2 name: ")

    current = 'X'

    if game < 4:
        size = [3,4,5][game-1]
        board = [' ']*(size*size)

        while True:
            clear(); draw_board(board, size)
            name = p1 if current == 'X' else p2

            if vs_ai and current == 'O':
                move = ai_easy(board) if ai_level == 1 else ai_hard(board, size, 'O', 'X')
                time.sleep(0.5)
            else:
                move = int(input(f"\n{name}'s move: ")) - 1

            if move < 0 or move >= size*size or board[move] != ' ': continue
            board[move] = current

            if check_win(board, size, current):
                clear(); draw_board(board, size)
                print(f"\n{name} WINS!\n\n\nPowered by:\n#S56 Companies\n#Naiver Companies\n"); break

            if board_full(board): print("\nDRAW!\n\n\nPowered by:\n#S56 Companies\n#Naiver Companies\n"); break
            current = switch_player(current)

    else:
        ub, bb = new_ultimate()
        forced_board = -1

        while True:
            clear(); show_ultimate(ub)
            name = p1 if current == 'X' else p2
            print(f"\n{name}'s turn")

            if forced_board == -1 or bb[forced_board] != ' ':
                if forced_board != -1 and bb[forced_board] != ' ':
                    print(f"Forced board {forced_board+1} is closed. Choose any open board.")
                if vs_ai and current == 'O':
                    open_boards = [i for i in range(9) if bb[i] == ' ']
                    b = random.choice(open_boards)
                else:
                    b = int(input("Choose board (1-9): ")) - 1
            else:
                b = forced_board
                print(f"You are forced to play on board {b+1}")

            if vs_ai and current == 'O':
                if ai_level == 1:
                    c = random.choice([i for i, v in enumerate(ub[b]) if v == ' '])
                else:
                    c = None
                    for i in range(9):
                        if ub[b][i] == ' ':
                            ub[b][i] = 'O'
                            if small_win(ub, b, 'O'):
                                ub[b][i] = ' '
                                c = i; break
                            ub[b][i] = ' '
                    if c is None:
                        for i in range(9):
                            if ub[b][i] == ' ':
                                ub[b][i] = 'X'
                                if small_win(ub, b, 'X'):
                                    ub[b][i] = ' '
                                    c = i; break
                                ub[b][i] = ' '
                    if c is None:
                        c = random.choice([i for i, v in enumerate(ub[b]) if v == ' '])
                time.sleep(0.5)
            else:
                c = int(input("Choose cell (1-9): ")) - 1

            if b < 0 or b > 8 or c < 0 or c > 8 or ub[b][c] != ' ': continue

            ub[b][c] = current

            if small_win(ub, b, current):
                bb[b] = current

            if big_win(bb, current):
                clear(); show_ultimate(ub)
                print(f"\n{name} wins ultimate Tic Tac Toe: Legends!\n\n\nPowered by:\n#S56 Companies\n#Naiver Companies\n")
                break

            forced_board = c
            current = switch_player(current)

if __name__ == '__main__':
    main()
