import pygame

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


class Chess:
    image = None
    actions = None

    @classmethod
    def draw(cls, screen, rect):
        image_rect = cls.image.get_rect(center=rect.center)
        screen.blit(cls.image, image_rect)

    @classmethod
    def get_actions(cls):
        return cls.actions

