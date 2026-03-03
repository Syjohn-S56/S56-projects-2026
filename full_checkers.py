import pygame
import sys
import time
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers Legends")

PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 102, 255)
DARK_BLUE = (0, 0, 139)

LIGHT_PURPLE = (216, 191, 255)
DARK_PURPLE = (75, 0, 130)
RED = (200, 0, 0)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

font_title = pygame.font.SysFont("verdana", 100, bold=True)
font_big = pygame.font.SysFont("verdana", 48, bold=True)
font_med = pygame.font.SysFont("verdana", 36, bold=True)
font_small = pygame.font.SysFont("verdana", 24, bold=True)
font_input = pygame.font.SysFont("verdana", 36, bold=True)

def draw_sponsors():
    sponsors = font_small.render("Sponsors:", True, MAGENTA)
    sponsor1 = font_small.render("#S56 Companies", True, MAGENTA)
    sponsor2 = font_small.render("#Naiver companies", True, MAGENTA)

    WIN.blit(sponsors, (20, HEIGHT - 120))
    WIN.blit(sponsor1, (20, HEIGHT - 80))
    WIN.blit(sponsor2, (20, HEIGHT - 40))

def transition(text):
    WIN.fill(PURPLE)

    label = font_big.render(text, True, BLACK)
    WIN.blit(label, (WIDTH//2 - label.get_width()//2,
                     HEIGHT//2 - label.get_height()//2))
    draw_sponsors()
    pygame.display.update()
    time.sleep(1)

def intro_screen():
    WIN.fill(PURPLE)

    title = font_title.render("S56 projects", True, BLACK)
    sponsors = font_small.render("Sponsors:", True, MAGENTA)
    sponsor1 = font_small.render("#S56 Companies", True, MAGENTA)
    sponsor2 = font_small.render("#Naiver companies", True, MAGENTA)

    WIN.blit(title, (WIDTH//2 - title.get_width()//2,
                     HEIGHT//2 - title.get_height()//2))
    WIN.blit(sponsors, (20, HEIGHT - 120))
    WIN.blit(sponsor1, (20, HEIGHT - 80))
    WIN.blit(sponsor2, (20, HEIGHT - 40))
    draw_sponsors()
    pygame.display.update()
    time.sleep(2)

def choose_checkers_type():
    while True:
        WIN.fill(PURPLE)

        welcome = font_big.render("Welcome to checker legends!", True, DARK_BLUE)
        prompt = font_med.render("Choose the type of checkers you want:", True, BLACK)
        option1 = font_small.render("1. Classic checkers", True, BLUE)
        option2 = font_small.render("2. Pro checkers", True, BLUE)
        center_y = HEIGHT//2 - 100
        start_x = WIDTH//2 - max(option1.get_width(), option2.get_width())//2

        WIN.blit(welcome, (WIDTH//2 - welcome.get_width()//2, center_y - 80))
        WIN.blit(prompt, (WIDTH//2 - prompt.get_width()//2, center_y - 20))
        WIN.blit(option1, (start_x, center_y + 40))
        WIN.blit(option2, (start_x, center_y + 80))
        draw_sponsors()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "Classic"
                if event.key == pygame.K_2:
                    return "Pro"

def choose_game_mode():
    while True:
        WIN.fill(PURPLE)

        prompt = font_med.render("Choose the game mode you want:", True, BLACK)
        option1 = font_small.render("1. Player vs Player", True, BLUE)
        option2 = font_small.render("2. Player vs AI", True, BLUE)
        center_y = HEIGHT//2 - 60
        start_x = WIDTH//2 - max(option1.get_width(), option2.get_width())//2

        WIN.blit(prompt, (WIDTH//2 - prompt.get_width()//2, center_y - 40))
        WIN.blit(option1, (start_x, center_y + 20))
        WIN.blit(option2, (start_x, center_y + 60))
        draw_sponsors()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "PvP"
                if event.key == pygame.K_2:
                    return "PvAI"
                
def input_names_pvp():
    player1 = ""
    player2 = ""
    active = 1
    clock = pygame.time.Clock()
    cursor_visible = True
    cursor_timer = 0

    while True:
        clock.tick(60)
        cursor_timer += 1
        if cursor_timer >= 30:
            cursor_visible = not cursor_visible
            cursor_timer = 0

        WIN.fill(PURPLE)

        title = font_big.render("Enter Player Names", True, BLACK)
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 200))

        p1_label = font_med.render("Player 1 (RED):", True, BLACK)
        p2_label = font_med.render("Player 2 (BLUE):", True, BLACK)

        WIN.blit(p1_label, (150, 350))
        WIN.blit(p2_label, (150, 420))

        display_p1 = player1
        display_p2 = player2

        if active == 1 and cursor_visible:
            display_p1 += "|"
        if active == 2 and cursor_visible:
            display_p2 += "|"

        text1 = font_input.render(display_p1, True, DARK_BLUE)
        text2 = font_input.render(display_p2, True, DARK_BLUE)

        WIN.blit(text1, (150 + p1_label.get_width() + 20, 350))
        WIN.blit(text2, (150 + p2_label.get_width() + 20, 420))
        draw_sponsors()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active == 1:
                        active = 2
                    else:
                        return player1 if player1 else "Player 1", \
                               player2 if player2 else "Player 2"

                elif event.key == pygame.K_BACKSPACE:
                    if active == 1:
                        player1 = player1[:-1]
                    else:
                        player2 = player2[:-1]

                else:
                    if active == 1:
                        player1 += event.unicode
                    else:
                        player2 += event.unicode


def input_name_pvai():
    name = ""
    clock = pygame.time.Clock()
    cursor_visible = True
    cursor_timer = 0

    while True:
        clock.tick(60)
        cursor_timer += 1
        if cursor_timer >= 30:
            cursor_visible = not cursor_visible
            cursor_timer = 0

        WIN.fill(PURPLE)
        title = font_big.render("Enter Your Name", True, BLACK)
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 250))
        label = font_med.render("Player (RED):", True, BLACK)
        WIN.blit(label, (200, 400))
        display_name = name
        if cursor_visible:
            display_name += "|"

        typed = font_input.render(display_name, True, DARK_BLUE)
        WIN.blit(typed, (200 + label.get_width() + 20, 400))
        draw_sponsors()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name if name else "Player"

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    name += event.unicode

def choose_ai_level():
    while True:
        WIN.fill(PURPLE)
        t = font_med.render("Choose AI Level", True, BLACK)
        o1 = font_small.render("1. Easy", True, BLUE)
        o2 = font_small.render("2. Hard", True, BLUE)

        WIN.blit(t, (WIDTH//2 - t.get_width()//2, 250))
        WIN.blit(o1, (WIDTH//2 - o1.get_width()//2, 350))
        WIN.blit(o2, (WIDTH//2 - o2.get_width()//2, 400))
        draw_sponsors()
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1: return "easy"
                if e.key == pygame.K_2: return "hard"

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

    def move(self, row, col):
        self.row, self.col = row, col

    def draw(self, win):
        center = (
            self.col*SQUARE_SIZE + SQUARE_SIZE//2,
            self.row*SQUARE_SIZE + SQUARE_SIZE//2
        )

        radius = SQUARE_SIZE//2 - 12

        pygame.draw.circle(win, (0,0,0), (center[0]+4, center[1]+4), radius)

        pygame.draw.circle(win, self.color, center, radius)

        pygame.draw.circle(win, WHITE,
                           (center[0]-radius//3, center[1]-radius//3),
                           radius//4)

        if self.king:
            crown = font_small.render("K", True, GOLD)
            win.blit(crown,
                     (center[0]-crown.get_width()//2,
                      center[1]-crown.get_height()//2))


class Board:
    def __init__(self, checkers_type):
        self.board = []
        self.checkers_type = checkers_type
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row+col)%2 != 0:
                    if row < 3:
                        self.board[row].append(Piece(row,col,BLUE))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        for y in range(HEIGHT):
            shade = 40 + int((y / HEIGHT) * 40)
            pygame.draw.line(win, (shade, 0, shade+40), (0, y), (WIDTH, y))

        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_PURPLE if (row+col)%2==0 else DARK_PURPLE
                pygame.draw.rect(win, color,
                                 (col*SQUARE_SIZE,
                                  row*SQUARE_SIZE,
                                  SQUARE_SIZE,
                                  SQUARE_SIZE))

        for row in self.board:
            for piece in row:
                if piece != 0:
                    piece.draw(win)

    def get_piece(self,row,col):
        return self.board[row][col]

    def move(self,piece,row,col):
        self.board[piece.row][piece.col]=0
        self.board[row][col]=piece
        piece.move(row,col)

        if piece.color==RED and row==0:
            piece.king=True
        if piece.color==BLUE and row==ROWS-1:
            piece.king=True

    def remove(self,captured):
        for r,c in captured:
            self.board[r][c]=0

    def get_all_pieces(self,color):
        return [p for row in self.board for p in row
                if p!=0 and p.color==color]

    def get_valid_moves(self, piece):
        moves = {}
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if piece.king:
            for dr, dc in directions:
                r = piece.row + dr
                c = piece.col + dc
                enemy = None
                while 0 <= r < ROWS and 0 <= c < COLS:
                    current = self.board[r][c]

                    if current == 0:
                        if enemy:
                            moves[(r, c)] = [(enemy.row, enemy.col)]
                        else:
                            moves[(r, c)] = []

                    elif current.color == piece.color:
                        break

                    else:
                        if enemy:
                            break
                        enemy = current

                    r += dr
                    c += dc

        else:
            if self.checkers_type == "Pro":
                move_dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]
            else:
                move_dirs = [(-1,-1), (-1,1)] if piece.color == RED else [(1,-1), (1,1)]

            for dr, dc in move_dirs:
                r = piece.row + dr
                c = piece.col + dc

                if 0 <= r < ROWS and 0 <= c < COLS:
                    current = self.board[r][c]

                    if current == 0:
                        if (piece.color == RED and dr == -1) or \
                           (piece.color == BLUE and dr == 1):
                            moves[(r, c)] = []

                    elif current.color != piece.color:
                        jr = r + dr
                        jc = c + dc

                        if 0 <= jr < ROWS and 0 <= jc < COLS:
                            if self.board[jr][jc] == 0:
                                moves[(jr, jc)] = [(r, c)]

        return moves

    def has_capture(self, color):
        for p in self.get_all_pieces(color):
            for m in self.get_valid_moves(p).values():
                if m:
                    return True
        return False

class Game:
    def __init__(self, mode, ai_level, player1, player2, checkers_type):
        self.board = Board(checkers_type)
        self.turn = RED
        self.selected = None
        self.valid_moves = {}
        self.mode = mode
        self.ai_level = ai_level
        self.checkers_type = checkers_type
        self.player_red = player1
        self.player_blue = player2
        self.draw_move_counter = 0
        self.draw_tracking_active = False
        self.must_continue = False

    def update(self):
        self.board.draw(WIN)
        if self.selected:
            pygame.draw.circle(WIN, YELLOW,
                (self.selected.col*SQUARE_SIZE+SQUARE_SIZE//2,
                 self.selected.row*SQUARE_SIZE+SQUARE_SIZE//2),
                 SQUARE_SIZE//2-5, 3)

            for move in self.valid_moves:
                r,c = move
                pygame.draw.circle(WIN, GOLD,
                    (c*SQUARE_SIZE+SQUARE_SIZE//2,
                     r*SQUARE_SIZE+SQUARE_SIZE//2), 10)

        current_name = self.player_red if self.turn == RED else self.player_blue
        label = font_small.render(f"{current_name}'s Turn", True, BLACK)
        WIN.blit(label, (20,20))

        pygame.display.update()

    def change_turn(self):
        self.selected = None
        self.valid_moves = {}
        self.must_continue = False
        if self.draw_tracking_active:
            self.draw_move_counter += 1

        self.turn = BLUE if self.turn == RED else RED

    def select(self, r, c):
        piece = self.board.get_piece(r,c)

        if self.must_continue:
            if (r,c) in self.valid_moves:
                self.execute_move(r,c)
            return

        if self.selected:
            if (r,c) in self.valid_moves:
                self.execute_move(r,c)
            else:
                self.selected = None

        elif piece!=0 and piece.color==self.turn:
            moves = self.board.get_valid_moves(piece)

            if self.board.has_capture(self.turn):
                moves = {m:c for m,c in moves.items() if c}

            if moves:
                self.selected = piece
                self.valid_moves = moves

    def execute_move(self, r, c):
        captured = self.valid_moves[(r, c)]
        piece = self.selected
        was_king = piece.king
        self.board.move(piece, r, c)
        just_promoted = (not was_king and piece.king)

        if captured:
            self.board.remove(captured)

            if just_promoted:
                self.change_turn()
                return

            new_moves = self.board.get_valid_moves(piece)
            capture_moves = {m: c for m, c in new_moves.items() if c}
            if capture_moves:
                if piece.king:
                    continuing_moves = {}
 
                    for move, cap in capture_moves.items():
                        temp_board = self.clone_board(self.board)
                        temp_piece = temp_board.get_piece(piece.row, piece.col)
                        temp_board.move(temp_piece, move[0], move[1])
                        temp_board.remove(cap)
                        next_moves = temp_board.get_valid_moves(temp_piece)
                        next_capture = {m: c for m, c in next_moves.items() if c}
  
                        if next_capture:
                            continuing_moves[move] = cap

                    if continuing_moves:
                        self.must_continue = True
                        self.selected = piece
                        self.valid_moves = continuing_moves
                        return

                self.must_continue = True
                self.selected = piece
                self.valid_moves = capture_moves
                return

        self.change_turn()

    def ai_move(self):
        if self.ai_level == "easy":
            pieces = self.board.get_all_pieces(BLUE)
            capture_moves = []
            normal_moves = []
            for p in pieces:
                moves = self.board.get_valid_moves(p)
                for move, cap in moves.items():
                    if cap:
                        capture_moves.append((p, move, cap))
                    else:
                        normal_moves.append((p, move, cap))

            if capture_moves:
                p, m, c = random.choice(capture_moves)
            else:
                p, m, c = random.choice(normal_moves)

            self._apply_ai_move(p, m, c)
            return

        best_score = -9999
        best_move = None
        depth = 6
        moves = self.get_all_moves(self.board, BLUE)
        for piece, move, captured in moves:
            temp_board = self.clone_board(self.board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            temp_board.move(temp_piece, move[0], move[1])
            promotion_move = False
            if not temp_piece.king and temp_piece.row == ROWS - 1:
                promotion_move = True

            total_captured = 0

            if captured:
                temp_board.remove(captured)
                total_captured += len(captured)
                last_dr = move[0] - piece.row
                while True:
                    next_moves = temp_board.get_valid_moves(temp_piece)
                    capture_moves = {}
                    for m, c in next_moves.items():
                        if c:
                            dr = m[0] - temp_piece.row

                            if (dr > 0 and last_dr > 0) or (dr < 0 and last_dr < 0):
                                capture_moves[m] = c

                    if capture_moves:
                        m2, c2 = max(capture_moves.items(), key=lambda x: len(x[1]))
                        temp_board.move(temp_piece, m2[0], m2[1])
                        temp_board.remove(c2)
                        total_captured += len(c2)
                        last_dr = m2[0] - temp_piece.row

                    else:
                        break

                while True:
                    next_moves = temp_board.get_valid_moves(temp_piece)
                    capture_moves = {}
                    for m, c in next_moves.items():
                        if c:
                            dr = m[0] - temp_piece.row
                            dc = m[1] - temp_piece.col
                            if (dr > 0 and last_dr > 0) or (dr < 0 and last_dr < 0):
                                capture_moves[m] = c

                    if capture_moves:
                        best_next_move = max(capture_moves.items(),
                                             key=lambda x: len(x[1]))
                        m2, c2 = best_next_move
                        temp_board.move(temp_piece, m2[0], m2[1])
                        temp_board.remove(c2)
                        total_captured += len(c2)
                    else:
                        break

            score = self.minimax(temp_board, depth-1, -9999, 9999, False)

            if self._would_be_captured(temp_board, temp_piece):
                score -= 12

            if total_captured <= 1 and self._would_be_captured(temp_board, temp_piece):
                score -= 8

            if temp_board.has_capture(RED):
                score -= 6

            if promotion_move:
                score += 14

                if not self._is_piece_in_danger(temp_board, temp_piece.row, temp_piece.col):
                    score += 6

            blue_count = len(self.board.get_all_pieces(BLUE))
            red_count = len(self.board.get_all_pieces(RED))
            if blue_count > red_count and captured:
                score += 5

            if temp_board.has_capture(RED) and score > 0:
                score += 2

            if score > best_score:
                if blue_count >= red_count and captured is None:
                    temp_blue = len(temp_board.get_all_pieces(BLUE))
                    temp_red = len(temp_board.get_all_pieces(RED))
                    if temp_blue < blue_count:
                        score -= 8
                best_score = score
                best_move = (piece, move, captured)

        if best_move:
            p, m, c = best_move
            self._apply_ai_move(p, m, c)

    def _apply_ai_move(self, p, m, c):
        self.board.move(p, m[0], m[1])
        if c:
            self.board.remove(c)
            if not p.king and (p.row == ROWS-1):
                p.king = True
                self.change_turn()
                return

            while True:
                moves = self.board.get_valid_moves(p)
                capture_moves = {m:cap for m,cap in moves.items() if cap}
                if capture_moves:
                    m, cap = max(capture_moves.items(),
                                 key=lambda x: len(x[1]))
                    self.board.move(p, m[0], m[1])
                    self.board.remove(cap)
                else:
                    break

        self.change_turn()

    def _is_piece_in_danger(self, board, row, col):
        red_pieces = board.get_all_pieces(RED)
        for p in red_pieces:
            moves = board.get_valid_moves(p)
            for move, captured in moves.items():
                if captured:
                    for r,c in captured:
                        if r == row and c == col:
                            return True
        return False

    def winner_on_board(self, board):
        if not board.get_all_pieces(RED):
            return self.player_blue
        if not board.get_all_pieces(BLUE):
            return self.player_red
        return None
    
    def winner(self):
        red_pieces = self.board.get_all_pieces(RED)
        blue_pieces = self.board.get_all_pieces(BLUE)
        if not red_pieces:
            return self.player_blue
        if not blue_pieces:
            return self.player_red
        if not self.has_any_moves(RED):
            return self.player_blue
        if not self.has_any_moves(BLUE):
            return self.player_red

        return None
    
    def _get_threatened_pieces(self):
        threatened = []
        red_pieces = self.board.get_all_pieces(RED)
        for red in red_pieces:
            moves = self.board.get_valid_moves(red)
            for move, captured in moves.items():
                if captured:
                    for r, c in captured:
                        threatened.append((r, c))
        return threatened
    
    def evaluate_board(self, board):
        blue_score = 0
        red_score = 0

        blue_pieces = board.get_all_pieces(BLUE)
        red_pieces = board.get_all_pieces(RED)
        total_pieces = len(blue_pieces) + len(red_pieces)
        for p in blue_pieces:
            if total_pieces <= 6:
                value = 7
                if p.king:
                    value = 15
            else:
                value = 5
                if p.king:
                    value = 9

            if self._is_piece_in_danger(board, p.row, p.col):
                value -= 4

            blue_score += value

            if total_pieces > 6:
                if 2 <= p.row <= 5 and 2 <= p.col <= 5:
                    blue_score += 1

        for p in blue_pieces:
            if p.row == ROWS - 1:
                blue_score += 1

        for p in red_pieces:
            if total_pieces <= 6:
                value = 7
                if p.king:
                    value = 15
            else:
                value = 5
                if p.king:
                    value = 9

            if self._is_piece_in_danger(board, p.row, p.col):
                value -= 4

            red_score += value

        for p in red_pieces:
            if p.row == 0:
                red_score += 1

        score = blue_score - red_score
        blue_moves = len(self.get_all_moves(board, BLUE))
        red_moves = len(self.get_all_moves(board, RED))
        if total_pieces > 6:
            score += 0.3 * (blue_moves - red_moves)
        else:
            score += 0.1 * (blue_moves - red_moves)

        return score
    
    def clone_board(self, board):
        import copy
        return copy.deepcopy(board)
    
    def get_all_moves(self, board, color):
        moves = []
        mandatory = board.has_capture(color)
        all_capture_counts = []
        for piece in board.get_all_pieces(color):
            valid = board.get_valid_moves(piece)
            if mandatory:
                valid = {m:c for m,c in valid.items() if c}

            for move, captured in valid.items():
                capture_len = len(captured) if captured else 0
                all_capture_counts.append(capture_len)
                moves.append((piece, move, captured, capture_len))

        if mandatory and all_capture_counts:
            max_cap = max(all_capture_counts)
            moves = [(p, m, c) for (p, m, c, l) in moves if l == max_cap]
        else:
            moves = [(p, m, c) for (p, m, c, l) in moves]

        return moves
    
    def minimax(self, board, depth, alpha, beta, maximizing):
        winner = self.winner_on_board(board)
        if depth == 0 or winner:
           return self.evaluate_board(board)

        if maximizing:
            max_eval = -9999
            moves = self.get_all_moves(board, BLUE)

            for piece, move, captured in moves:
                temp_board = self.clone_board(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                temp_board.move(temp_piece, move[0], move[1])
                if captured:
                    temp_board.remove(captured)
                    last_dr = move[0] - piece.row
                    while True:
                        next_moves = temp_board.get_valid_moves(temp_piece)
                        capture_moves = {}
                        for m, c in next_moves.items():
                            if c:
                               dr = m[0] - temp_piece.row
                               if (dr > 0 and last_dr > 0) or (dr < 0 and last_dr < 0):
                                   capture_moves[m] = c

                        if capture_moves:
                            m2, c2 = max(capture_moves.items(), key=lambda x: len(x[1]))
                            temp_board.move(temp_piece, m2[0], m2[1])
                            temp_board.remove(c2)
                            last_dr = m2[0] - temp_piece.row

                        else:
                            break
                    while True:
                        next_moves = temp_board.get_valid_moves(temp_piece)
                        capture_moves = {}
                        for m, c in next_moves.items():
                            if c:
                                dr = m[0] - temp_piece.row
                                dc = m[1] - temp_piece.col
                                if (dr > 0 and last_dr > 0) or (dr < 0 and last_dr < 0):
                                    capture_moves[m] = c
                        if capture_moves:
                            m2, c2 = max(capture_moves.items(), key=lambda x: len(x[1]))
                            temp_board.move(temp_piece, m2[0], m2[1])
                            temp_board.remove(c2)
                        else:
                            break

                eval = self.minimax(temp_board, depth-1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval

        else:
            min_eval = 9999
            moves = self.get_all_moves(board, RED)

            for piece, move, captured in moves:
                temp_board = self.clone_board(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                temp_board.move(temp_piece, move[0], move[1])
                if captured:
                    temp_board.remove(captured)
                    while True:
                        next_moves = temp_board.get_valid_moves(temp_piece)
                        capture_moves = {m:c for m,c in next_moves.items() if c}
                        if capture_moves:
                            m2, c2 = max(capture_moves.items(), key=lambda x: len(x[1]))
                            temp_board.move(temp_piece, m2[0], m2[1])
                            temp_board.remove(c2)
                        else:
                            break

                eval = self.minimax(temp_board, depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval
        
    def _would_be_captured(self, board, piece):
        enemy_color = RED if piece.color == BLUE else BLUE
        enemies = board.get_all_pieces(enemy_color)
        for e in enemies:
            moves = board.get_valid_moves(e)
            for move, captured in moves.items():
                if captured:
                    for r, c in captured:
                        if r == piece.row and c == piece.col:
                            return True
        return False
    
    def update_draw_status(self):
        red_pieces = self.board.get_all_pieces(RED)
        blue_pieces = self.board.get_all_pieces(BLUE)
        total = len(red_pieces) + len(blue_pieces)
        red_kings = [p for p in red_pieces if p.king]
        blue_kings = [p for p in blue_pieces if p.king]
        if total <= 4:
            if len(red_pieces) == len(blue_pieces):
                if all(p.king for p in red_pieces + blue_pieces):
                    return "DRAW"

        if total <= 5 and red_kings and blue_kings:
            self.draw_tracking_active = True
        else:
            self.draw_tracking_active = False
            self.draw_move_counter = 0

        if self.draw_tracking_active:
            if self.draw_move_counter >= 30:
                return "DRAW"

        return None
    
    def has_any_moves(self, color):
        for piece in self.board.get_all_pieces(color):
            moves = self.board.get_valid_moves(piece)
            if self.board.has_capture(color):
                moves = {m:c for m,c in moves.items() if c}

            if moves:
                return True
        return False
    
def show_rules(checkers_type):
    WIN.fill(PURPLE)
    if checkers_type == "Classic":
        title_text = "Here are the rules for Classic Checkers"
        rule1 = "1. It's forward capturing only."
    else:
        title_text = "Here are the rules for Pro Checkers"
        rule1 = "1. It's both forward and backward capturing."

    rule2 = "2. It's mandatory to capture."
    rule3 = "3. Multi-capturing is also mandatory."
    rule4 = "4. Kings(Flying) promotion available."

    title = font_med.render(title_text, True, BLACK)
    r1 = font_small.render(rule1, True, BLUE)
    r2 = font_small.render(rule2, True, BLUE)
    r3 = font_small.render(rule3, True, BLUE)
    r4 = font_small.render(rule4, True, BLUE)

    WIN.blit(title, (WIDTH//2 - title.get_width()//2, 200))
    WIN.blit(r1, (150, 300))
    WIN.blit(r2, (150, 340))
    WIN.blit(r3, (150, 380))
    WIN.blit(r4, (150, 420))
    draw_sponsors()
    pygame.display.update()
    time.sleep(8)


def main():
    intro_screen()
    checkers_type = choose_checkers_type()
    mode = choose_game_mode()
    player1 = None
    player2 = None
    ai_level = "easy"

    if mode == "PvP":
        player1, player2 = input_names_pvp()
    else:
        player1 = input_name_pvai()
        ai_level = choose_ai_level()
        player2 = "Bonk AI"

    show_rules(checkers_type)
    transition("Loading Game...")
    game = Game(mode, ai_level, player1, player2, checkers_type)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        if mode == "PvAI" and game.turn == BLUE:
            game.ai_move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == "PvP" or (mode == "PvAI" and game.turn == RED):
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // SQUARE_SIZE
                    col = pos[0] // SQUARE_SIZE
                    game.select(row, col)

        game.update()

        draw_state = game.update_draw_status()
        if draw_state == "DRAW":
            transition("GAME DRAW!")
            run = False
            break

        winner_name = game.winner()
        if winner_name:
            transition(f"{winner_name} WINS!")
            run = False
            break

    pygame.quit()
    sys.exit()

main()