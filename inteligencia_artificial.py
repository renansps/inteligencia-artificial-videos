import cv2
import dlib
import numpy as np

# Carregar a imagem escolhida pelo usuário
img_path = input("Insira o caminho da imagem: ")
img = cv2.imread(img_path)

# Carregar o vídeo
video_path = input("Insira o caminho do vídeo: ")
cap = cv2.VideoCapture(video_path)

# Detector de faces do dlib
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar faces no frame
    faces = detector(frame)

    # Loop pelas faces detectadas
    for face in faces:
        # Obter a região da face
        x, y = face.left(), face.top()
        w, h = face.right() - x, face.bottom() - y

        # Redimensionar a imagem escolhida para o tamanho da face
        img_resized = cv2.resize(img, (w, h))

        # Substituir a face no frame com a imagem escolhida
        frame[y:y+h, x:x+w] = img_resized

    # Mostrar o frame com a face substituída
    cv2.imshow('Video', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()