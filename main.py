import pygame, sys
from color import Colors
from board import Board

screen = pygame.display.set_mode(size=(900, 700))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

cell_size = 60

board = Board(cell_size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(Colors.SILVER)
    board.draw(screen)
    
    pygame.display.update()
    clock.tick(60)