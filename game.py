from grid import Grid
import pygame
from color import Colors
from pieces import *

cell_size = 60

class Game:
    pieces = dict(zip(range(1, 13), [WhiteKing, WhiteQueen, WhiteRook, WhiteKnight, WhiteBishop, WhitePawn, BlackKing, BlackQueen, BlackRook, BlackKnight, BlackBishop, BlackPawn]))

    def __init__(self):
        self.grid = Grid()
        self.pressed = False
        self.suggest = []
        self.pressed_cell = None

    def draw(self, screen):
        for num in range(64):
            row, col = num//8, num%8
            
            cell_color = [Colors.SILVER, Colors.WHITE][(row+col)%2]
            cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, cell_color, cell_rect)

            id = self.grid[row][col]
            if id > 0: 
                self.pieces[id].draw(screen, cell_rect)

        if self.pressed_cell != None:
            for position in self.suggest:
                center_x = position[1] * cell_size + cell_size // 2
                center_y = position[0] * cell_size + cell_size // 2
                
                if self.grid[position[0]][position[1]] == 0:
                    pygame.draw.circle(screen, Colors.SLATE_GRAY, (center_x, center_y), 10)
                else:
                    id1 = self.grid[self.pressed_cell[0]][self.pressed_cell[1]]
                    id2 = self.grid[position[0]][position[1]]
                    if (1 <= min(id1, id2) <= 6) and (7 <= max(id1, id2) <= 12):
                        pygame.draw.circle(screen, Colors.SLATE_GRAY, (center_x, center_y), 28, 5)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.in_game(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                if self.pressed_cell == None:
                    self.pressed_cell = self.get_pressed_cell(mouse_pos)
                else:
                    current_cell = self.get_pressed_cell(mouse_pos)
                    self.grid[current_cell[0]][current_cell[1]] = self.grid[self.pressed_cell[0]][self.pressed_cell[1]]
                    self.grid[self.pressed_cell[0]][self.pressed_cell[1]] = 0
                    self.pressed_cell = None

                id = self.grid[self.pressed_cell[0]][self.pressed_cell[1]]

                if id:
                    self.suggest = Game.pieces[id].valid_positions(self.pressed_cell, self.grid)
                # for pos in moves:
                #     center_x = pos[1] * cell_size + cell_size // 2
                #     center_y = pos[0] * cell_size + cell_size // 2
                #     self.suggest.append((center_x, center_y))

                return True
    
        if not mouse_pressed:
            self.pressed = False 
            # self.pressed_cell = None
        return False 



    def get_pressed_cell(self, mouse_pos):
        row = mouse_pos[1] // cell_size
        col = mouse_pos[0] // cell_size
        return (row, col)
    
    def in_game(self, mouse_pos):
        if (0 <= mouse_pos[0] < 480) and (0 <= mouse_pos[1] < 480): 
            return True
        return False

