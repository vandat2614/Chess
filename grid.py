import pygame
from color import Colors
from chess_pieces import *

class Grid:
    def __init__(self, cell_size=60):
        self.cell_size = cell_size
        self.num_rows = 8
        self.num_cols = 8
        self.reset()
        self.chess_pieces = [King(id=1), King(id=2), Queen(id=3), Queen(id=4), Rook(id=5), Rook(id=6), 
                             Knight(id=7), Knight(id=8), Bishop(id=9), Bishop(id=10), Pawn(id=11), Pawn(id=12)]

    def reset(self):
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.grid[0] = [6, 8, 10, 4, 2, 10, 8, 6]
        self.grid[1] = [12] * 8
        self.grid[self.num_rows-2] = [11] * 8
        self.grid[self.num_rows-1] = [5, 7, 9, 3, 1, 9, 7, 5] 

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_rows):

                cell_color = [Colors.SILVER, Colors.WHITE][(row+col)%2]
                cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, cell_color, cell_rect)

                id = self.grid[row][col]
                if id > 0: 
                    self.chess_pieces[id-1].draw(screen, cell_rect)

                if id == -1:
                    x = col * self.cell_size + 30
                    y = row * self.cell_size + 30
                    pygame.draw.circle(screen, Colors.SLATE_GRAY, (x, y), 20)

    def __getitem__(self, row):
        return self.grid[row]

