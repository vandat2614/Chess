from grid import Grid
import pygame
from piece import Chess

cell_size = 60

class Game:

    def __init__(self):
        self.grid = Grid(cell_size)
        self.pressed = False

        self.current_cell = None
        self.turn = Chess.WHITE

    def draw(self, screen):
        self.grid.draw(screen)

        if self.current_cell != None and self.turn == Chess.type(self.grid[self.current_cell[0]][self.current_cell[1]]):
            self.grid.draw_suggests(screen, self.current_cell)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.in_game(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True

                pressed_cell = self.get_pressed_cell(mouse_pos)
                value = self.grid[pressed_cell[0]][pressed_cell[1]]

                if self.current_cell == None:
                    if value != 0:
                        self.current_cell = pressed_cell
                elif not self.grid.valid_move(self.current_cell, pressed_cell):
                    self.current_cell = pressed_cell
                else:
                    current_id = self.grid[self.current_cell[0]][self.current_cell[1]]
                    if Chess.type(current_id) == self.turn:
                        self.grid.move(self.current_cell, pressed_cell)
                        self.current_cell = None
                        self.change_turn()

        if not mouse_pressed:
            self.pressed = False 

        return self.pressed 

    def get_pressed_cell(self, mouse_pos):
        row = mouse_pos[1] // cell_size
        col = mouse_pos[0] // cell_size
        return (row, col)
    
    def in_game(self, mouse_pos):
        if (0 <= mouse_pos[0] < 480) and (0 <= mouse_pos[1] < 480): 
            return True
        return False

    def change_turn(self):
        self.turn = 1 - self.turn