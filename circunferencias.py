import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('MOTORv4.jpg')
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un desenfoque para reducir el ruido
imagen_desenfocada = cv2.GaussianBlur(imagen_gris, (9, 9), 2)

# Detectar círculos usando la Transformada de Hough
circulos = cv2.HoughCircles(imagen_desenfocada, cv2.HOUGH_GRADIENT, 1, 100,
                            param1=250, param2=30, minRadius=20, maxRadius=60)

# Dibujar los círculos detectados en la imagen original
if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")
    for (x, y, r) in circulos:
        cv2.circle(imagen, (x, y), r, (0, 255, 0), 4)

# Mostrar la imagen con los círculos detectados
cv2.imshow('Círculos Detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
