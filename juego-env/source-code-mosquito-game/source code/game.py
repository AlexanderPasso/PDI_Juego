#Importanto las librerias necesarias
import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from mosquito import Mosquito
from bee import Bee
import cv2
import ui

# Define una clase llamada Game para gestionar el juego.
class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Inicialización de la cámara
        self.cap = cv2.VideoCapture(0)

        # Inicialización de los sonidos del juego
        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"source-code-mosquito-game/source code/Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"source-code-mosquito-game/source code/Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)

    # Método para reiniciar todas las variables necesarias del juego.
    def reset(self):
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()

    # Método para generar insectos en el juego en momentos específicos.
    def spawn_insects(self):
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + MOSQUITOS_SPAWN_TIME

            # Aumenta la probabilidad de que el insecto sea una abeja con el tiempo.
            nb = (GAME_DURATION - self.time_left) / GAME_DURATION * 100 / 2  # aumenta de 0 a 50 durante todo el juego (lineal)
            if random.randint(0, 100) < nb:
                self.insects.append(Bee())
            else:
                self.insects.append(Mosquito())

            # Genera otro mosquito después de la mitad del juego.
            if self.time_left < GAME_DURATION / 2:
                self.insects.append(Mosquito())

    # Método para cargar imágenes de la cámara.
    def load_camera(self):
        _, self.frame = self.cap.read()

    # Método para establecer la posición de la mano en el juego.
    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    # Método para dibujar elementos en la pantalla del juego.
    def draw(self):
        # Dibuja el fondo.
        self.background.draw(self.surface)
        # Dibuja los insectos.
        for insect in self.insects:
            insect.draw(self.surface)
        # Dibuja la mano.
        self.hand.draw(self.surface)
        # Dibuja la puntuación.
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255, 255, 255))
        # Dibuja el tiempo restante.
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"]  # cambia el color del texto si quedan menos de 5 segundos
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH // 2, 5), timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255, 255, 255))

    # Método para actualizar el tiempo de juego.
    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)

    # Método para actualizar el estado del juego.
    def update(self):
        self.load_camera()          #Carga la camara
        self.set_hand_position()    #Obtener la posicion de la mano
        self.game_time_update()     #Actualizar el tiempo del juego
        self.draw()                 #Actualiza las imagenes en ela pantalla

        if self.time_left > 0:
            self.spawn_insects()                        # Genera insectos en el juego
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed

            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()

            self.score = self.hand.kill_insects(self.insects, self.score, self.sounds)
            for insect in self.insects:
                insect.move()                       # Mueve los insectos en la pantalla
        else:  # Cuando el juego ha terminado
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["slap"]):
                return "menu"

        cv2.imshow("Frame", self.frame)             #Muestra el frame de la cámara en una ventana
        cv2.waitKey(1)                              ## Espera 1 milisegundo (útil para mantener la ventana de la cámara abierta)
