import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2


# Define una clase llamada Hand para representar una mano en el juego.
class Hand:
    def __init__(self):
        # Carga la imagen original de la mano con un tamaño específico.
        self.orig_image = image.load("source-code-mosquito-game/source code/Assets/hand.png", size=(HAND_SIZE, HAND_SIZE))

        # Crea una copia de la imagen original.
        self.image = self.orig_image.copy()

        # Carga una versión más pequeña de la imagen de la mano.
        self.image_smaller = image.load("source-code-mosquito-game/source code/Assets/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))


        # Crea un rectángulo para representar la "hitbox" (zona de colisión) de la mano.
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])

        # Inicializa una variable para verificar si se hizo clic con el botón izquierdo del mouse.
        self.left_click = False


    def follow_mouse(self):    # Cambia la posición del centro de la mano a la posición actual del mouse.
        self.rect.center = pygame.mouse.get_pos()


    def follow_mediapipe_hand(self, x, y):      # Cambia la posición del centro de la mano a las coordenadas (x, y) proporcionadas.
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):             # Dibuja un rectángulo en la superficie para representar la "hitbox" de la mano.
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

  
    def draw(self, surface):                    # Dibuja la imagen de la mano en la superficie con la posición del rectángulo como centro.
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:                         # Si DRAW_HITBOX está activado en la configuración, dibuja la "hitbox".
            self.draw_hitbox(surface)


    def on_insect(self, insects):               # Devuelve una lista de todos los insectos que colisionan con la "hitbox" de la mano.
        return [insect for insect in insects if self.rect.colliderect(insect.rect)]


    def kill_insects(self, insects, score, sounds):       # Mata a los insectos que colisionan con la mano cuando se presiona el botón izquierdo del mouse.
        if self.left_click: # if left click
            for insect in self.on_insect(insects):
                insect_score = insect.kill(insects)
                score += insect_score
                sounds["slap"].play()
                if insect_score < 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
