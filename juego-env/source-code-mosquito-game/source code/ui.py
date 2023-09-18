import pygame
from settings import *

# Función para dibujar texto en la pantalla
def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
                shadow=False, shadow_color=(0,0,0), shadow_offset=2):
    # Crea una superficie de texto con el contenido 'text' y el color especificado
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    
    # Ajusta la posición del texto según el modo especificado
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow:  # Crea una sombra para el texto si está habilitada
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect)  # Dibuja el texto en la superficie

# Función para crear un botón interactivo
def button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2, pos_y), BUTTONS_SIZES)

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):  # Comprueba si el cursor del mouse está sobre el botón
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    # Dibuja un rectángulo sombreado para el botón
    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h))
    pygame.draw.rect(surface, color, rect)  # Dibuja el rectángulo del botón

    # Dibuja el texto en el botón si se proporciona un texto
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                    shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]:  # Comprueba si se hizo clic en el botón
        if click_sound is not None:  # Reproduce el sonido de clic si se proporciona
            click_sound.play()
        return True

