from grid import Grid
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.current_cell = None

        self.pressed = False
        self.pressed_cell = None
        self.valid_options = None
        
    def get_pos(self):
        return pygame.mouse.get_pos()

    def draw(self, screen):
        self.grid.draw(screen)

    def get_valid_piece_options(self, cell):
        return [(cell[0]-1, cell[1]), (cell[0]-2, cell[1])]

    def get_pressed_cell(self, mouse_pos):
        row = mouse_pos[1] // 60
        col = mouse_pos[0] // 60
        return (row, col)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if (0 <= mouse_pos[0] <= 480) and (0 <= mouse_pos[1] <= 480):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                self.pressed_cell = self.get_pressed_cell(mouse_pos)
                self.valid_options = self.get_valid_piece_options(self.pressed_cell)

                for (row, col) in self.valid_options:
                    self.grid[row][col] = -1

                return True

        if not mouse_pressed:
            self.pressed = False 

        return False 
