import pygame
import sys
from settings import *
from background import Background
import ui

# Definición de la clase Menu
class Menu:
    def __init__(self, surface):
        # Constructor de la clase, recibe una superficie 'surface' para dibujar el menú
        self.surface = surface
        self.background = Background()  # Creación de una instancia de la clase Background para gestionar el fondo
        self.click_sound = pygame.mixer.Sound(f"source-code-mosquito-game/source code/Assets/Sounds/slap.wav")  # Carga de un sonido de clic

    def draw(self):
        # Método para dibujar el menú en la superficie 'self.surface'
        self.background.draw(self.surface)  # Dibuja el fondo
        # Dibuja el título en el centro de la pantalla con sombreado
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255, 255, 255), pos_mode="center")

    def update(self):
        # Método para actualizar el menú en cada ciclo del juego
        self.draw()  # Llamada al método 'draw' para dibujar el menú
        # Verifica si se hizo clic en el botón "START" y retorna "game" si es así
        if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
            return "game"
        # Verifica si se hizo clic en el botón "Quit", y si es así, cierra el juego
        if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "Quit", click_sound=self.click_sound):
            pygame.quit()
            sys.exit()

