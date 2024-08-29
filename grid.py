from pieces import *
from color import Colors
import pygame

class Grid:
    pieces = dict(zip(range(1, 13), [WhiteKing, WhiteQueen, WhiteRook, WhiteKnight, WhiteBishop, WhitePawn, BlackKing, BlackQueen, BlackRook, BlackKnight, BlackBishop, BlackPawn]))

    def __init__(self, cell_size=60):
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.grid = [[0] * 8 for _ in range(8)]
        self.grid[0] = [Chess.WHITE_ROOK, Chess.WHITE_KNIGHT, Chess.WHITE_BISHOP, Chess.WHITE_QUEEN, Chess.WHITE_KING, Chess.WHITE_BISHOP, Chess.WHITE_KNIGHT, Chess.WHITE_ROOK]
        self.grid[1] = [Chess.WHITE_PAWN] * 8

        self.grid[6] = [Chess.BLACK_PAWN] * 8
        self.grid[7] = [Chess.BLACK_ROOK, Chess.BLACK_KNIGHT, Chess.BLACK_BISHOP, Chess.BLACK_QUEEN, Chess.BLACK_KING, Chess.BLACK_BISHOP, Chess.BLACK_KNIGHT, Chess.BLACK_ROOK] 

    def draw(self, screen):
        for num in range(64):
            row, col = num//8, num%8
            
            cell_color = [Colors.SILVER, Colors.WHITE][(row+col)%2]
            cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, cell_color, cell_rect)

            id = self.grid[row][col]
            if id > 0: 
                Grid.pieces[id].draw(screen, cell_rect)
    
    def draw_suggests(self, screen, position):
        current_id = self.grid[position[0]][position[1]]
        if current_id == 0:
            return
        suggests = Grid.pieces[current_id].valid_positions(position, self.grid)
        for new_pos in suggests:
            center_x = new_pos[1] * self.cell_size + self.cell_size//2
            center_y = new_pos[0] * self.cell_size + self.cell_size//2

            next_id = self.grid[new_pos[0]][new_pos[1]]
            
            if Chess.is_opponent(current_id, next_id):
                radius, width = 28, 5
            else: radius, width = 10, 0

            pygame.draw.circle(screen, Colors.SLATE_GRAY, (center_x, center_y), radius, width)

    def valid_move(self, old_pos, new_pos):
        old_id = self.grid[old_pos[0]][old_pos[1]]
        if old_id == 0:
            return False
        valid_positions = Grid.pieces[old_id].valid_positions(old_pos, self.grid)
        if new_pos in valid_positions:
            return True
        return False

    def move(self, old_pos, new_pos):
        self.grid[new_pos[0]][new_pos[1]] = self.grid[old_pos[0]][old_pos[1]]
        self.grid[old_pos[0]][old_pos[1]] = 0

    def __getitem__(self, row):
        return self.grid[row]