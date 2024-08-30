from grid import Grid
import pygame
from pieces import *
from theme import Theme
from color import Colors

class Game:

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = Grid(cell_size)

        self.pressed = False
        self.current_cell = None
        self.winner = None

        self.turn = Chess.WHITE
        self.theme = 0

    def reset(self):
        self.grid.reset()
        self.pressed = False
        self.current_cell = None
        self.turn = Chess.WHITE
        self.winner = None

    def draw(self, screen):
        self.grid.draw_board(screen, Theme.get_theme(self.theme))

        if self.grid.have_promotion():
            self.grid.draw_promotion_select(screen, Theme.get_theme(3), self.change_turn())

        if self.current_cell != None:
            if self.turn == Chess.type(self.grid[self.current_cell[0]][self.current_cell[1]]):
                self.grid.draw_suggests(screen, self.current_cell)
    
    def draw_winner_announce(self, screen):
        if self.winner == Chess.BLACK:
            winner = 'Black'
        else: winner = 'White'

        title_font = pygame.font.Font(None, 65)
        text = f'{winner} player is the winner'
        
        text_surface = title_font.render(text, True, Colors.BLUE)
        screen.blit(text_surface, (self.cell_size-35, 4*self.cell_size-23, 50, 50))

    def handle_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.in_game(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True

                pressed_cell = self.get_pressed_cell(mouse_pos)
                value = self.grid[pressed_cell[0]][pressed_cell[1]]

                if self.grid.have_promotion() and self.winner == None:
                    if self.turn == Chess.BLACK:
                        promotions = [[Chess.WHITE_QUEEN, Chess.WHITE_ROOK], [Chess.WHITE_BISHOP, Chess.WHITE_KNIGHT]]
                    else: promotions = [[Chess.BLACK_QUEEN, Chess.BLACK_ROOK], [Chess.BLACK_BISHOP, Chess.BLACK_KNIGHT]]
                    
                    if 3 <= pressed_cell[0] <= 4 and 3 <= pressed_cell[1] <= 4:
                        promotion_id = promotions[pressed_cell[0] - 3][pressed_cell[1] - 3]
                        self.grid.promotion(promotion_id)

                if self.current_cell == None:
                    if value != 0:
                        self.current_cell = pressed_cell
                elif not self.grid.valid_move(self.current_cell, pressed_cell):
                    self.current_cell = pressed_cell
                else:
                    current_id = self.grid[self.current_cell[0]][self.current_cell[1]]
                    if Chess.type(current_id) == self.turn and self.grid.is_safe_move(self.current_cell, pressed_cell):
                        self.grid.move(self.current_cell, pressed_cell)
                        self.current_cell = None
                        self.turn = self.change_turn()
                        self.winner = self.grid.get_winner()

                
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
        if self.turn == Chess.BLACK:
            return Chess.WHITE
        return Chess.BLACK
    
    def increase_theme(self):
        self.theme = (self.theme + 1) % Theme.num

    def decrease_theme(self):
        self.theme = self.theme - 1
        if self.theme == -1:
            self.theme = Theme.num - 1
