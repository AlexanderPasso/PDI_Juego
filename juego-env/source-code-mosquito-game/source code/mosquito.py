import pygame
import random
import time
import image
from settings import *

# Definición de la clase Mosquito
class Mosquito:
    def __init__(self):
        # Generación aleatoria del tamaño del mosquito
        random_size_value = random.uniform(MOSQUITO_SIZE_RANDOMIZE[0], MOSQUITO_SIZE_RANDOMIZE[1])
        size = (int(MOSQUITOS_SIZES[0] * random_size_value), int(MOSQUITOS_SIZES[1] * random_size_value))
        
        # Definición de la dirección de movimiento y la posición de inicio del mosquito
        moving_direction, start_pos = self.define_spawn_pos(size)
        
        # Creación de un rectángulo que representa al mosquito en la pantalla
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        
        # Carga de imágenes del mosquito para su animación
        self.images = [image.load("source-code-mosquito-game/source code/Assets/mosquito/mosquito.png", size=size, flip=moving_direction=="right")]
        
        # Inicialización de variables para la animación
        self.current_frame = 0
        self.animation_timer = 0

    def define_spawn_pos(self, size):
        # Definición de la posición de inicio y la velocidad de movimiento del mosquito
        vel = random.uniform(MOSQUITOS_MOVE_SPEED["min"], MOSQUITOS_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        
        return moving_direction, start_pos

    def move(self):
        # Mueve el mosquito en función de su velocidad actual
        self.rect.move_ip(self.vel)

    def animate(self):
        # Cambia el cuadro de la animación del insecto cuando es necesario
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0

    def draw_hitbox(self, surface):
        # Dibuja la caja de colisión (hitbox) del mosquito en la pantalla
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        # Dibuja el mosquito en la superficie, incluyendo su animación y, opcionalmente, su hitbox
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def kill(self, mosquitos):
        # Elimina el mosquito de la lista de mosquitos y devuelve 1
        mosquitos.remove(self)
        return 1

