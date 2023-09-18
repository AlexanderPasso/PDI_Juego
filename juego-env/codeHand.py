import cv2
import mediapipe as mp

# Configuración de Mediapipe para dibujar y detectar manos
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Para la entrada de la cámara web:
cap = cv2.VideoCapture(0)

# Inicializa el modelo de detección de manos con ciertas confianzas mínimas
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignorando fotograma vacío de la cámara.")
      # Si se carga un video, usa 'break' en lugar de 'continue'.
      continue
    # Voltea la imagen horizontalmente para una vista de selfie posterior y convierte
    # la imagen BGR a RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # Para mejorar el rendimiento, opcionalmente marca la imagen como no escribible
    # para pasarla por referencia.
    image.flags.writeable = False
    results = hands.process(image)
    # Dibuja las anotaciones de la mano en la imagen.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    cv2.imshow('MediPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

