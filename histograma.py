#librerias utilizadas
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#imagen 320x240
    
img = Image.open("tigre.jpg")  #lee la imagen
matriz = np.array(img)  #convierte la imagen en un arreglo
filas,columnas,dimensiones = matriz.shape # filas, columnas y dimensiones de la matriz

plt.imshow(img)  #muestra la imagen original

#separa la imagen en sus 3 colores rgb
r, g, b = img.split()

#obtiene la matriz de colores
matriz_rojo = np.array(r)
matriz_verde = np.array(g)
matriz_azul = np.array(b)

# ------------------------ HISTOGRAMA DE IMAGEN ---------------------------
def histograma(matriz, filas, columnas):
    hist = [0]*256  # llena de 0 las 256 posiciones del arreglo
    for k in range(256):  # recorre los 256 niveles de gris
        cont = 0
        for i in range(0,filas):  # dimensiones de x de la imagen 
            for j in range(0,columnas):  # dimensiones en y de la imagen
                if(matriz[i][j] == k):   # compara si en alguna de las coordenadas es igual al valor de gris
                    cont = cont + 1   # suma 1 al contador si es verdadero
        hist[k] = cont   # asigna ese valor al vector del histograma
    return hist  # retorna el histograma

# ------------------------ PLOTEO DE LOS HISTOGRAMAS ---------------------------
def ploteo(matriz_rojo,matriz_verde,matriz_azul, filas, columnas):
    #guarda los vectores del histograma correspondientes a cada canal
    rojo = histograma(matriz_rojo, filas, columnas)
    verde = histograma(matriz_verde, filas, columnas)
    azul = histograma(matriz_azul, filas, columnas)

    #une los 3 canales 
    plt.plot(rojo, color='red')
    plt.plot(verde, color='green')
    plt.plot(azul, color='blue')

    plt.show()  #imprime la grafica resultante
    
ploteo(matriz_rojo,matriz_verde,matriz_azul, filas, columnas)
