import pygame

class Chess:
    image = None
    WHITE = 1
    BLACK = 2
    EMPTY = 0

    
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
    def get_pices(cls, type):
        if type == Chess.WHITE:
            pieces = [cls.WHITE_KING, cls.WHITE_QUEEN, cls.WHITE_ROOK, cls.WHITE_KNIGHT, cls.WHITE_BISHOP, cls.WHITE_PAWN]
        else: 
            pieces = [cls.BLACK_KING, cls.BLACK_QUEEN, cls.BLACK_ROOK, cls.BLACK_KNIGHT, cls.BLACK_BISHOP, cls.BLACK_PAWN]

        return pieces

    @classmethod
    def is_opponent(cls, id1, id2):
        type1 = Chess.type(id1)
        type2 = Chess.type(id2)

        if type1 == Chess.EMPTY or type2 == Chess.EMPTY:
            return False

        if type1 == type2:
            return False
        
        return True
    
    @classmethod
    def type(cls, id):
        if id in Chess.get_pices(Chess.BLACK):
            return Chess.BLACK

        if id in Chess.get_pices(Chess.WHITE):
            return Chess.WHITE
        
        return Chess.EMPTY
    

def read_image(image_path, scale_factor=0.1):
    origin_image = pygame.image.load(image_path)
    image = scale_image(origin_image, scale_factor)
    return image
        
def scale_image(image, scale_factor=1):
    original_width = image.get_width()
    original_height = image.get_height()

    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    return pygame.transform.smoothscale(image, (new_width, new_height))

def valid_position(position):
    if (0 <= position[0] <= 7) and (0 <= position[1] <= 7):
        return True
    return False
