from grid import Grid
import pygame
from color import Colors
from pieces import *

cell_size = 60

class Game:
    pieces = dict(zip(range(1, 13), [BlackKing, BlackQueen, BlackRook, BlackKnight, BlackBishop, BlackPawn, WhiteKing, WhiteQueen, WhiteRook, WhiteKnight, WhiteBishop, WhitePawn]))

    def __init__(self):
        self.grid = Grid()
        self.pressed = False

    def draw(self, screen):
        for num in range(64):
            row, col = num//8, num%8
            
            cell_color = [Colors.SILVER, Colors.WHITE][(row+col)%2]
            cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, cell_color, cell_rect)

            id = self.grid[row][col]
            if id > 0: 
                self.pieces[id].draw(screen, cell_rect)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if Game.in_game(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                self.pressed_cell = Game.get_pressed_cell(mouse_pos)
                print(self.pressed_cell)
                return True
    
        if not mouse_pressed:
            self.pressed = False 
        return False 

    @classmethod
    def get_pressed_cell(cls, mouse_pos):
        row = mouse_pos[1] // cell_size
        col = mouse_pos[0] // cell_size
        return (row, col)
    
    @classmethod
    def in_game(cls, mouse_pos):
        if (0 <= mouse_pos[0] < 480) and (0 <= mouse_pos[1] < 480): 
            return True
        return False