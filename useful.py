import pygame


def get_scale(screen: pygame.surface.Surface, image: pygame.surface.Surface):
    # szerokość okna / oryginalna szerokość obrazka
    scale_x = screen.get_width() / image.get_width()
    scale_y = screen.get_height() / image.get_height()
    return scale_x, scale_y


def scale_image(image: pygame.surface.Surface, scale_x, scale_y):
    """Funkcja skaluje podany obraz image przez wartości skali scale_x i
    scale_y."""
    _image = pygame.transform.scale(image,
                                    (image.get_width() * scale_x,
                                     image.get_height() * scale_y))
    return _image


def load_scale_image(path, img_name, scale_x, scale_y):
    """Funkcja wczytuje z podanej ścierzki path obraz img_name i skaluje go
    przez podane skale scale_x i scale_y."""
    path = path
    img = pygame.image.load(f"{path}/{img_name}")
    img = scale_image(img, scale_x, scale_y)
    return img
