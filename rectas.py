import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('MOTORv4.jpg')
if imagen is None:
    print("Error: no se pudo cargar la imagen. Verifique la ruta del archivo.")
    exit()

# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes (Canny)
bordes = cv2.Canny(imagen_gris, 50, 150, apertureSize=3)

# Usar la Transformada de Hough para detectar líneas
lineas = cv2.HoughLines(bordes, 1, np.pi / 100, 120)

# Dibujar las líneas en la imagen
if lineas is not None:
    for linea in lineas:
        rho, theta = linea[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen
cv2.imshow('Líneas Detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
