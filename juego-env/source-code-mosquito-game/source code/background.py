
#Importando las librerias necesarias
import pygame
import image
from settings import *

#Definicion de la clase que me permite cargar y mostrar el fondo del juego
class Background:
    def __init__(self):
        self.image = image.load("source-code-mosquito-game/source code/Assets/background.jpg", size=(SCREEN_WIDTH, SCREEN_HEIGHT),   #Cargo la imagen, con el tamaño definido en settings.
                                convert="default")


    def draw(self, surface): #Permite dibujar el fondo en la superficie 
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")  #Este metodo dibuja la imagen de fondo en la posicion especificada
