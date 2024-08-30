import pygame, sys
from color import Colors
from game import Game

pygame.init()
cell_size = 80

screen = pygame.display.set_mode(size=(8*cell_size, 8*cell_size))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

title_font = pygame.font.Font(None, 65)

game = Game(cell_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.increase_theme()
            elif event.key == pygame.K_RIGHT:
                game.decrease_theme()
            elif event.key == pygame.K_r:
                game.reset()

    screen.fill(Colors.BLUE)
    game.draw(screen)
    if game.winner != None:
        if game.winner == 0:
            text = 'White player is the winner'
        else: text = 'Black player is the winner'


        text_surface = title_font.render(text, True, Colors.BLUE)
        screen.blit(text_surface, (cell_size-35, 4*cell_size-23, 50, 50))
    else: game.handle_pressed()

    # for r in range(2):
    #     for c in range(2):
    #         promotion_rect = pygame.Rect(cell_size*3 + cell_size * c, cell_size*3 + cell_size * r, cell_size , cell_size)
    #         if (r+c)%2 == 0:
    #             color = (255, 69, 0)
    #         else: color = Colors.BLUE
    #         pygame.draw.rect(screen, color, promotion_rect)


    pygame.display.update()
    clock.tick(60)