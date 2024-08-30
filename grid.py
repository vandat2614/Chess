from pieces import *
from color import Colors
import pygame

class Grid:
    pieces = dict(zip(range(1, 13), [WhiteKing, WhiteQueen, WhiteRook, WhiteKnight, WhiteBishop, WhitePawn, BlackKing, BlackQueen, BlackRook, BlackKnight, BlackBishop, BlackPawn]))

    def __init__(self, cell_size=60):
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.grid = [[Chess.EMPTY] * 8 for _ in range(8)]

        self.grid[0] = [Chess.BLACK_ROOK, Chess.BLACK_KNIGHT, Chess.BLACK_BISHOP, Chess.BLACK_QUEEN, Chess.BLACK_KING, Chess.BLACK_BISHOP, Chess.BLACK_KNIGHT, Chess.BLACK_ROOK] 
        self.grid[1] = [Chess.BLACK_PAWN] * 8

        self.grid[6] = [Chess.WHITE_PAWN] * 8
        self.grid[7] = [Chess.WHITE_ROOK, Chess.WHITE_KNIGHT, Chess.WHITE_BISHOP, Chess.WHITE_QUEEN, Chess.WHITE_KING, Chess.WHITE_BISHOP, Chess.WHITE_KNIGHT, Chess.WHITE_ROOK]

    def draw_board(self, screen, bg_colors):
        for cell in range(64):
            row, col = cell//8, cell%8
            
            cell_color = bg_colors[(row+col)%2]
            cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)

            pygame.draw.rect(screen, cell_color, cell_rect)

            id = self.grid[row][col]
            if id != Chess.EMPTY: 
                Grid.pieces[id].draw(screen, cell_rect)

    def draw_suggests(self, screen, position):
        current_id = self.grid[position[0]][position[1]]

        if current_id == Chess.EMPTY:
            return
        
        suggests = Grid.pieces[current_id].valid_positions(position, self.grid)

        for new_pos in suggests:
            if self.is_safe_move(position, new_pos):
                center_x = new_pos[1] * self.cell_size + self.cell_size//2
                center_y = new_pos[0] * self.cell_size + self.cell_size//2

                next_id = self.grid[new_pos[0]][new_pos[1]]
                
                if Chess.is_opponent(current_id, next_id):
                    radius, width = 35, 5
                else: radius, width = 15, 0

                pygame.draw.circle(screen, (173,216,230), (center_x, center_y), radius, width)

    def is_safe_move(self, old_pos, new_pos):
        old_id = self.grid[old_pos[0]][old_pos[1]]
        new_id = self.grid[new_pos[0]][new_pos[1]]

        self.move(old_pos, new_pos)

        safe = False
        if self.is_safe(Chess.type(old_id)):
            safe = True

        self.grid[old_pos[0]][old_pos[1]] = old_id
        self.grid[new_pos[0]][new_pos[1]] = new_id

        return safe

    def promotion(self, promotion_id):
        for col in range(8):
            if self.grid[0][col] == Chess.WHITE_PAWN:
                self.grid[0][col] = promotion_id

            if self.grid[7][col] == Chess.BLACK_PAWN:
                self.grid[7][col] = promotion_id

    def have_promotion(self):
        for col in range(8):
            if self.grid[0][col] == Chess.WHITE_PAWN or self.grid[7][col] == Chess.BLACK_PAWN:
                return True
        return False

    def draw_promotion_select(self, screen, bg_colors, turn):
        offset_x = offset_y = self.cell_size * 3

        if turn == Chess.BLACK:
            promotion_pieces = [BlackQueen, BlackRook, BlackBishop, BlackKnight]
        else: promotion_pieces = [WhiteQueen, WhiteRook, WhiteBishop, WhiteKnight]

        for cell in range(4):
            row, col = cell//2, cell%2
            cell_rect = pygame.Rect(offset_x + col * self.cell_size, offset_y + row * self.cell_size, self.cell_size, self.cell_size)
            cell_color = bg_colors[(row+col)%2]
    
            pygame.draw.rect(screen, cell_color, cell_rect)
            promotion_pieces[cell].draw(screen, cell_rect)

    def valid_move(self, old_pos, new_pos):
        old_id = self.grid[old_pos[0]][old_pos[1]]

        if old_id == Chess.EMPTY:
            return False
        
        valid_positions = Grid.pieces[old_id].valid_positions(old_pos, self.grid)
        if new_pos in valid_positions:
            return True
        
        return False

    def move(self, old_pos, new_pos):
        self.grid[new_pos[0]][new_pos[1]] = self.grid[old_pos[0]][old_pos[1]]
        self.grid[old_pos[0]][old_pos[1]] = Chess.EMPTY
    

    def __getitem__(self, row):
        return self.grid[row]
    
    def is_live(self, type):
        for cell in range(64):
            row, col = cell//8, cell%8
            id = self.grid[row][col]
            if id == type:
                return True
        return False

    def get_winner(self):        
        if self.get_king_position(Chess.WHITE) == None:
            return Chess.BLACK        
        elif self.get_king_position(Chess.BLACK) == None:
            return Chess.WHITE
        else: return None

    def get_king_position(self, type):
        if type == Chess.BLACK:
            target = Chess.BLACK_KING
        else:
            target = Chess.WHITE_KING

        for cell in range(64):
            row, col = cell//8, cell%8
            if self.grid[row][col] == target:
                return (row, col)
            
        return None
    
    def is_safe(self, type):
        king_pos = self.get_king_position(type)

        for cell in range(64):
            row, col = cell//8, cell%8
            cell_id = self.grid[row][col]
            
            if cell_id == 0:
                continue

            cell_type = Chess.type(cell_id)
            if cell_type != type and king_pos in Grid.pieces[cell_id].valid_positions((row, col), self.grid):
                return False
        
        return True

