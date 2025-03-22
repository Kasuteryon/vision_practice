
import cv2
import numpy as np

# Captura de la imagen desde la cámara
cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Imagen de referencia', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):  # Presiona 's' para guardar la imagen
        cv2.imwrite('referencia.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()

# Cargar imagen de referencia
image = cv2.imread('referencia.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Encontrar contornos
contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos = sorted(contornos, key=cv2.contourArea, reverse=True)  # Ordenar por tamaño

# Dibujar contornos y calcular dimensiones
for contorno in contornos[:1]:  # Tomar el más grande
    (x, y), radius = cv2.minEnclosingCircle(contorno)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(image, center, radius, (0, 255, 0), 2)

cv2.imshow('Moneda Detectada', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definir el diámetro real de la moneda de referencia (en cm)
real_diameter_cm = 2.8  # 28 mm = 2.8 cm

# Obtener el diámetro en píxeles del contorno detectado
diameter_px = radius * 2  # Diámetro de la moneda en píxeles

# Calcular la relación píxeles por cm
pixels_per_cm = diameter_px / real_diameter_cm
print(f"1 cm equivale a {pixels_per_cm:.2f} píxeles")

# Medir otro objeto en la imagen
new_object_width_px = 150  # Ejemplo
real_size_cm = new_object_width_px / pixels_per_cm
print(f"El objeto mide aproximadamente {real_size_cm:.2f} cm")

"""

#tamaño de objeto cuadrado/rectangular

import cv2
import numpy as np

# Captura de la imagen desde la cámara
cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Imagen de referencia', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):  # Presiona 's' para guardar la imagen
        cv2.imwrite('referencia.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()

# Cargar imagen de referencia
image = cv2.imread('referencia.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Encontrar contornos
contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos = sorted(contornos, key=cv2.contourArea, reverse=True)  # Ordenar por tamaño

# Dibujar contornos y calcular dimensiones
for contorno in contornos[:1]:  # Tomar el más grande
    # Obtener el rectángulo de área mínima
    rect = cv2.minAreaRect(contorno)
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    # Dibujar el rectángulo en la imagen
    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

    # Calcular el ancho y alto del rectángulo
    width = int(rect[1][0])  # Ancho
    height = int(rect[1][1])  # Alto

    print(f"Dimensiones del rectángulo (en píxeles): Ancho = {width}, Alto = {height}")

# Mostrar la imagen con el contorno del rectángulo
cv2.imshow('Objeto Detectado', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definir una medida real para la referencia (en cm)
real_width_cm = 45  # Ejemplo, el ancho real del objeto en cm
real_height_cm = 37  # Ejemplo, el alto real del objeto en cm

# Calcular la relación píxeles por cm para cada dimensión
pixels_per_cm_width = width / real_width_cm
pixels_per_cm_height = height / real_height_cm

# Medir otro objeto en la imagen
new_object_width_px = 60  # Ejemplo
new_object_height_px = 67  # Ejemplo

# Convertir las medidas de píxeles a cm usando la relación de píxeles por cm
new_object_width_cm = new_object_width_px / pixels_per_cm_width
new_object_height_cm = new_object_height_px / pixels_per_cm_height

print(f"El nuevo objeto mide aproximadamente {new_object_width_cm:.2f} cm de ancho y {new_object_height_cm:.2f} cm de alto")
"""

