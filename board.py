import pygame
from color import Colors

# vua - 1
# hau - 2
# xe - 3
# ma - 4
# tuong - 5
# tot 6

class Board:
    def __init__(self, cell_size=60):
        self.cell_size = cell_size
        self.num_rows = 8
        self.num_cols = 8


        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.grid[0] = self.grid[self.num_rows-1] = [3, 4, 5, 2, 1, 5, 4, 3]
        self.grid[1] = self.grid[self.num_rows-2] = [6] * self.num_cols

    def draw(self, screen):

        image = pygame.image.load('chess.png')
        original_width = image.get_width()
        original_height = image.get_height()

        scale = 0.1
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        image = pygame.transform.smoothscale(image, (new_width, new_height))

        for row in range(self.num_rows):
            for col in range(self.num_rows):

                if (row+col)%2 == 0:
                    cell_color = Colors.SILVER
                else: cell_color = Colors.WHITE

                cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, cell_color, cell_rect)
                
                if self.grid[row][col] == 4 or True:
                    image_rect = image.get_rect(center=cell_rect.center)
                    screen.blit(image, image_rect)

