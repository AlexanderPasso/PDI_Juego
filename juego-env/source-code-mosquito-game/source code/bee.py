#Importanto las librerias
import pygame
import random
import image
from settings import *
from mosquito import Mosquito

#Se define la clase Bee que hereda de la clase Mosquito
class Bee(Mosquito):
    def __init__(self):
        #Se define un tamaño aleatorio para la abeja
        random_size_value = random.uniform(BEE_SIZE_RANDOMIZE[0], BEE_SIZE_RANDOMIZE[1])
        size = (int(BEE_SIZES[0] * random_size_value), int(BEE_SIZES[1] * random_size_value))
        # Direccion de movimiento y posicion de inicio para la abeja
        moving_direction, start_pos = self.define_spawn_pos(size)
        # creacion del rectangulo de la abeja
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)

        #Carga de las imagen de la abeja
        self.images = [image.load(f"source-code-mosquito-game/source code/Assets/bee/{nb}.png", size=size, flip=moving_direction=="right") for nb in range(1, 7)] # load the images

        #Inicializacion de variables para la animacion de la abeja
        self.current_frame = 0
        self.animation_timer = 0
        
    #Metodo para eliminar la abeja de la lista 
    def kill(self, mosquitos): 
        mosquitos.remove(self)
        return -BEE_PENALITY   #Resta 1 a la puntuacion general para penalizar
