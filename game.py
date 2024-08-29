from grid import Grid
import pygame
from piece import Chess
from theme import Theme

class Game:

    def __init__(self, cell_size):
        self.grid = Grid(cell_size)
        self.pressed = False
        self.cell_size = cell_size

        self.current_cell = None
        self.turn = Chess.WHITE
        self.theme = 0
        self.winner = None

    def reset(self):
        self.grid.reset()
        self.pressed = False
        self.current_cell = None
        self.turn = Chess.WHITE
        self.winner = None

    def draw(self, screen):
        self.grid.draw(screen, Theme.get_theme(self.theme))

        if self.current_cell != None and self.turn == Chess.type(self.grid[self.current_cell[0]][self.current_cell[1]]):
            self.grid.draw_suggests(screen, self.current_cell)

    def handle_pressed(self):
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
                        self.winner = self.grid.get_winner()
                        print(self.winner)

        if not mouse_pressed:
            self.pressed = False 

        return self.pressed 

    def get_pressed_cell(self, mouse_pos):
        row = mouse_pos[1] // self.cell_size
        col = mouse_pos[0] // self.cell_size
        return (row, col)
    
    def in_game(self, mouse_pos):
        if (0 <= mouse_pos[0] < self.cell_size*8) and (0 <= mouse_pos[1] < self.cell_size*8): 
            return True
        return False

    def change_turn(self):
        self.turn = 1 - self.turn

    def increase_theme(self):
        self.theme = (self.theme + 1) % Theme.num

    def decrease_theme(self):
        self.theme = self.theme - 1
        if self.theme == -1:
            self.theme = Theme.num - 1
