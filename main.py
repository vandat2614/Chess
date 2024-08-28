import pygame, sys
from color import Colors
from game import Game

screen = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()


game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(Colors.SILVER)

    if game.is_pressed():
        pass
    game.draw(screen)


    pygame.display.update()
    clock.tick(60)