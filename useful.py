import pygame


def get_scale(screen: pygame.surface.Surface, image: pygame.surface.Surface):
    # szerokość okna / oryginalna szerokość obrazka
    scale_x = screen.get_width() / image.get_width()
    scale_y = screen.get_height() / image.get_height()
    return scale_x, scale_y


def scale_image(image: pygame.surface.Surface, scale_x, scale_y):
    _image = pygame.transform.scale(image,
                                    (image.get_width() * scale_x,
                                     image.get_height() * scale_y))
    return _image
