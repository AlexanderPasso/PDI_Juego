import pygame


# Define una función llamada "load" para cargar una imagen.

def load(img_path, size="default", convert="alpha", flip=False):
    if convert == "alpha":
        img = pygame.image.load(img_path).convert_alpha()         # Carga la imagen y conserva la transparencia.
    else:
        img = pygame.image.load(img_path).convert()              # Carga la imagen y la convierte a un formato sin transparencia.

    if flip:
        img = pygame.transform.flip(img, True, False)            # Voltea la imagen horizontalmente si se especifica.

    if size != "default":
        img = scale(img, size)                                   # Escala la imagen a un tamaño específico si se especifica.

    return img


# Define una función llamada "scale" para escalar una imagen.
def scale(img, size):
    return pygame.transform.smoothscale(img, size)              # Escala la imagen de manera suave al tamaño deseado.


# Define una función llamada "draw" para dibujar una imagen en una superficie.
def draw(surface, img, pos, pos_mode="top_left"):
    if pos_mode == "center":
        pos = list(pos)
        pos[0] -= img.get_width()//2                            # Ajusta la posición para que el centro de la imagen coincida con "pos".
        pos[1] -= img.get_height()//2

    surface.blit(img, pos)                                      # Dibuja la imagen en la superficie en la posición especificada.
