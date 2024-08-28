import pygame

class Chess:
    colors = ['black', 'white']
    def __init__(self, id, name):
        self.id = id
        color = self.colors[id%2]

        image_path = f'Images\\{color}_{name}.png'
        self.read_image(image_path, scale_factor=0.1)
        
    def read_image(self, image_path, scale_factor=1):
        origin_image = pygame.image.load(image_path)
        self.image = self.scale_image(origin_image, scale_factor)
        
    def scale_image(self, image, scale_factor=1):
        original_width = image.get_width()
        original_height = image.get_height()

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        return pygame.transform.smoothscale(image, (new_width, new_height))

    def draw(self, screen, rect):
        image_rect = self.image.get_rect(center=rect.center)
        screen.blit(self.image, image_rect)