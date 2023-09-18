import pygame

# Nombre de la ventana del juego
WINDOW_NAME = "Machete Mata a Machete"
GAME_TITLE = WINDOW_NAME

# Dimensiones de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

# FPS (cuadros por segundo) del juego y opción para dibujar los FPS
FPS = 90
DRAW_FPS = True

# Tamaños predefinidos para varios elementos del juego
BUTTONS_SIZES = (240, 90)  # Tamaño de los botones
HAND_SIZE = 200  # Tamaño de la mano del jugador
HAND_HITBOX_SIZE = (60, 80)  # Tamaño de la caja de colisión de la mano
MOSQUITOS_SIZES = (50, 38)  # Tamaño de los mosquitos
MOSQUITO_SIZE_RANDOMIZE = (1, 2)  # Para cada nuevo mosquito, su tamaño se multiplicará por un valor aleatorio entre X e Y
BEE_SIZES = (50, 50)  # Tamaño de las abejas
BEE_SIZE_RANDOMIZE = (1.2, 1.5)  # Factor de aleatorización del tamaño de las abejas

# Configuración de dibujo, opción para dibujar las cajas de colisión (hitbox)
DRAW_HITBOX = False

# Velocidad de animación
ANIMATION_SPEED = 0.08  # La animación de los insectos cambiará de cuadro cada X segundos

# Dificultad del juego
GAME_DURATION = 60  # Duración del juego en segundos
MOSQUITOS_SPAWN_TIME = 1  # Intervalo de tiempo para la generación de mosquitos
MOSQUITOS_MOVE_SPEED = {"min": 1, "max": 5}  # Velocidad de movimiento de los mosquitos (mínima y máxima)
BEE_PENALITY = 1  # Restará X puntos de la puntuación del jugador si mata a una abeja

# Colores predefinidos utilizados en el juego
COLORS = {"title": (38, 61, 39),  # Color del título
          "score": (38, 61, 39),  # Color de la puntuación
          "timer": (38, 61, 39),  # Color del temporizador
          "buttons": {"default": (56, 67, 209),  # Color predeterminado de los botones
                      "second": (87, 99, 255),  # Color cuando el ratón está sobre el botón
                      "text": (255, 255, 255),  # Color del texto en los botones
                      "shadow": (46, 54, 163)}}  # Color de la sombra en los botones

# Volumen para la música y los sonidos
MUSIC_VOLUME = 0.16  # Valor entre 0 y 1 para el volumen de la música
SOUNDS_VOLUME = 1  # Valor entre 0 y 1 para el volumen de los sonidos

# Inicialización de fuentes de texto con tamaños predefinidos
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)  # Fuente pequeña
FONTS["medium"] = pygame.font.Font(None, 72)  # Fuente mediana
FONTS["big"] = pygame.font.Font(None, 120)  # Fuente grande

