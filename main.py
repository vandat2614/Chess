import pygame, sys
from color import Colors
from game import Game
from button import Button

pygame.init()
cell_size = 60

screen = pygame.display.set_mode(size=(8*cell_size, 8*cell_size + 60))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

button_width = cell_size*2

move_back_button = Button((0, 8*cell_size+5), button_width, 50)
move_back_button.config(text='Move back')

move_forward_button = Button((8*cell_size-button_width, 8*cell_size+5), button_width, 50)
move_forward_button.config(text='Move forward')

new_game_button = Button((button_width+cell_size, 8*cell_size+5), button_width, 50)
new_game_button.config(text='New game')

hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
default_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)

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
        game.draw_winner_announce(screen)
    else: game.handle_pressed()

    if move_back_button.is_hovered() or move_forward_button.is_hovered() or new_game_button.is_hovered():
        pygame.mouse.set_cursor(hand_cursor)
    else: pygame.mouse.set_cursor(default_cursor)    

    move_back_button.draw(screen)
    move_forward_button.draw(screen)
    new_game_button.draw(screen)

    if move_back_button.is_clicked():
        game.move_back()
    
    if move_forward_button.is_clicked():
        game.move_forward()

    if new_game_button.is_clicked():
        game.reset()


    pygame.display.update()
    clock.tick(60)