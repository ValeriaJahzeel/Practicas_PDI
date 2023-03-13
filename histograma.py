"""
Hecho por: Valeria Castañon
Fecha: 02 - marzo - 2023
Nombre: histograma.ipynb

Programa que realiza el histograma a una imagen RGB
y lo muestra en pantalla, sin utilizar los comandos
disponibles en python

"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#imagen 320x240    
img = Image.open("capibaraAjedrecista.png")  #lee la imagen
matriz = np.array(img)  #convierte la imagen en un arreglo
filas,columnas,dimensiones = matriz.shape # filas, columnas y dimensiones de la matriz

#separa la imagen en sus 3 colores rgb
r, g, b = img.split()

#obtiene la matriz de colores
matriz_rojo = np.array(r)
matriz_verde = np.array(g)
matriz_azul = np.array(b)

print(matriz_rojo.shape)

# convierte la matriz de cada canal RBG a una imagen
imagen_rojo = Image.fromarray(matriz_rojo)
imagen_verde = Image.fromarray(matriz_verde)
imagen_azul = Image.fromarray(matriz_azul)

# muestra las imagenes
axes=[]
fig=plt.figure()

axes.append(fig.add_subplot(2, 2, 1))  # muestra la imagen original
axes[0].set_title("Imagen original")  
plt.imshow(img)

axes.append(fig.add_subplot(2, 2, 2))  # muestra el canal rojo
axes[1].set_title("Canal rojo")  
plt.imshow(imagen_rojo)

axes.append(fig.add_subplot(2, 2, 3))  # muestra el canal verde
axes[2].set_title("Canal verde")  
plt.imshow(imagen_verde)

axes.append(fig.add_subplot(2, 2, 4))  #muestra el canal azul
axes[3].set_title("Canal azul")  
plt.imshow(imagen_azul)

fig.tight_layout()
plt.show

# ------------------------ HISTOGRAMA DE IMAGEN ---------------------------
def histograma(matriz, filas, columnas):
    hist = [0]*256  # llena de 0 las 256 posiciones del arreglo
    for k in range(256):  # recorre los 256 niveles de gris
        cont = 0
        for i in range(filas):  # dimensiones de x de la imagen 
            for j in range(columnas):  # dimensiones en y de la imagen
                if(matriz[i][j] == k):   # compara si en alguna de las coordenadas es igual al valor de gris
                    cont = cont + 1   # suma 1 al contador si es verdadero
                    #hist[k] = cont   # asigna ese valor al vector del histograma
        hist[k] = cont   # asigna ese valor al vector del histograma
    return hist  # retorna el histograma

# ------------------------ PLOTEO DE LOS HISTOGRAMAS ---------------------------
def ploteo(matriz_rojo,matriz_verde,matriz_azul, filas, columnas):
    #guarda los vectores del histograma correspondientes a cada canal
    rojo = histograma(matriz_rojo, filas, columnas)
    verde = histograma(matriz_verde, filas, columnas)
    azul = histograma(matriz_azul, filas, columnas)
    
    plt.title('Histograma')
    plt.xlabel('Niveles de gris')
    plt.ylabel('Frecuencia')
    
    #une los 3 canales 
    plt.plot(rojo, color='red')
    plt.plot(verde, color='green')
    plt.plot(azul, color='blue')

    plt.show()  #imprime la grafica resultante
