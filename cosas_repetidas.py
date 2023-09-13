# librerias
# Tomar una imagen RGB y convertirla a HSL y HSV
#se importan las librerias
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# colocar varias imagenes en una
# cmap="gray" es para imprimir la imagen en escala de grises
plt.subplot(1, 3, 1)
plt.imshow(hl, cmap="gray")
plt.title("H")

plt.subplot(1, 3, 2)
plt.imshow(ll, cmap="gray")
plt.title("L")

plt.subplot(1, 3, 3)
plt.imshow(sl, cmap="gray")
plt.title("V")

plt.show()


# abrir una imagen, separar sus canales RGB y sacar sus vectores
# Se abre la imagen y se obtiene la matriz
img = Image.open("capi.jpg")
matriz = np.array(img)
ancho, alto = img.size

# Se separa la imagen en los canales RGB
r, g, b = img.split()

# Se obtienen las matrices de los canales de color
matriz_rojo = np.array(r)
matriz_verde = np.array(g)
matriz_azul = np.array(b)

plt.imshow(img)