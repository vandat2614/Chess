import pygame

def read_image(image_path, scale_factor=0.08):
    origin_image = pygame.image.load(image_path)
    image = scale_image(origin_image, scale_factor)
    return image
        
def scale_image(image, scale_factor=1):
    original_width = image.get_width()
    original_height = image.get_height()

    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    return pygame.transform.smoothscale(image, (new_width, new_height))


class Chess:
    image = None
    
    BLACK_KING = 7
    BLACK_QUEEN = 8
    BLACK_ROOK = 9
    BLACK_KNIGHT = 10
    BLACK_BISHOP = 11
    BLACK_PAWN = 12

    WHITE_KING = 1
    WHITE_QUEEN = 2
    WHITE_ROOK = 3
    WHITE_KNIGHT = 4
    WHITE_BISHOP = 5
    WHITE_PAWN = 6

    @classmethod
    def draw(cls, screen, rect):
        image_rect = cls.image.get_rect(center=rect.center)
        screen.blit(cls.image, image_rect)
    
    @classmethod
    def valid_positions(cls, position, grid):
        pass
