#https://jhovhapdi.blogspot.com/2016/10/las-transformaciones-mas-simples-son_31.html
"""
Hecho por: Valeria Castañon
Fecha: 11 - marzo - 2023
Nombre: transformaciones_aritmeticas.ipynb

Programa que aplica las transformaciones aritmeticas de
- Suma
- Resta
- Multiplicacion
- Division
- Gamma 
- Inversa
- Ecualizacion
a una imagen RGB y posteriormente muestra su histograma

"""

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
    
#guarda las imagenes en cada espectro rgb
#r.save("canal_rojo.png")
#g.save("canal_verde.png")
#b.save("canal_azul.png")

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

# ------------------------ TRANSFORMACION DE SUMA ---------------------------
def suma(matriz,filas, columnas,val):
    #val es la cantidad a sumar
    suma = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            suma[x,y] = matriz[x,y] + val  # hace el proceso de suma

            if(suma[x,y] > 255):
                suma[x,y] = 255
            elif(suma[x,y] < 0):
                suma[x,y] = 0      
    return suma

# ------------------------ TRANSFORMACION DE RESTA ---------------------------
def resta(matriz,filas, columnas,val):
    #val es la cantidad a restar
    resta = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            resta[x,y] = matriz[x,y] - val  # hace el proceso de suma

            if(resta[x,y] > 255):
                resta[x,y] = 255
            elif(resta[x,y] < 0):
                resta[x,y] = 0        
    return resta

# ------------------------ TRANSFORMACION DE MULTIPLICACION ---------------------------
def multiplicacion(matriz,filas, columnas,val):
    #val es la cantidad a multiplicar
    multi = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            multi[x,y] = matriz[x,y] * val  # hace el proceso de suma

            if(multi[x,y] > 255):
                multi[x,y] = 255
            elif(multi[x,y] < 0):
                multi[x,y] = 0   
    return multi

# ------------------------ TRANSFORMACION DE DIVISION ---------------------------
def division(matriz,filas, columnas,val):
    #val es la cantidad a dividir
    div = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            div[x,y] = matriz[x,y] / val  # hace el proceso de suma

            if(div[x,y] > 255):
                div[x,y] = 255
            elif(div[x,y] < 0):
                div[x,y] = 0         
    return div

# ------------------------ TRANSFORMACION GAMMA ---------------------------
def gamma(matriz,filas, columnas,val):
    #val es la cantidad a aplicar gamma
    gamma = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    const = 0.08
    c = 255/255**const
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            gamma[x,y] = c*matriz[x,y]**const  # hace el proceso de gamma

            if(gamma[x,y] > 255):
                gamma[x,y] = 255
            elif(gamma[x,y] < 0):
                gamma[x,y] = 0         
    return gamma

# ------------------------ TRANSFORMACION INVERSA ---------------------------
def inversa(matriz,filas,columnas):
    #inversa de la matriz
    inversa = np.zeros((filas, columnas))  # llena de 0 la matriz del tamaño de la imagen
    
    for x in range(0,filas):  # eje x -> filas
        for y in range(0,columnas):  # eje y -> columnas
            inversa[x,y] = 255-matriz[x,y] # resta 255 a los valores de cada celda
    return inversa


# ------------------------ MENU DE OPCIONES ---------------------------
def menu(matriz_rojo, matriz_verde, matriz_azul, filas, columnas, dimensiones):
    print("""MENU:
           [1.] Suma 
           [2.] Resta
           [3.] Multiplicacion
           [4.] Division 
           [5.] Gamma 
           [6.] Inversa 
           [7.] Ecualizacion""")
    opc = int(input("Elige una opcion: "))  #permite al usuario elegir la opcion a realizar
    
    if opc==1:  # suma
        val = int(input("Cantidad a sumar: "))
        
        # pruebas para la suma - matrices
        prueba_rojo = suma(matriz_rojo, filas, columnas, val)
        prueba_verde = suma(matriz_verde, filas, columnas, val)
        prueba_azul = suma(matriz_azul, filas, columnas, val)
        
        # histograma de la imagen modificada
        ploteo(prueba_rojo,prueba_verde,prueba_azul, filas, columnas)

        # matriz que contiene la nueva imagen 
        union_imgs = np.zeros((filas,columnas,dimensiones), dtype=np.uint8)
        
        # Asigna valores a cada canal de color
        union_imgs[:,:,0] = prueba_rojo  # valores de rojo
        union_imgs[:,:,1] = prueba_verde  # valores de verde
        union_imgs[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(union_imgs)

        # Guarda la imagen en un archivo
        imagen_rgb.save("suma.png")
        print("Imagen lista")
        plt.imshow(imagen_rgb)
        
    elif opc==2:  # resta
        val = int(input("Cantidad a restar: "))
        # pruebas para la suma - matrices
        prueba_rojo = resta(matriz0, f0, c0, val)
        prueba_verde = resta(matriz1, f1, c1, val)
        prueba_azul = resta(matriz2, f2, c2, val)

        # histograma de las imagenes
        hist_rojo = histograma(m0_tam, prueba_rojo)
        hist_verde = histograma(m1_tam, prueba_verde)
        hist_azul = histograma(m2_tam, prueba_azul)
        
        imagen_nueva = np.zeros((f,c,3), dtype=np.uint8)
        # Asigna valores a cada canal de color
        imagen_nueva[:,:,0] = prueba_rojo  # valores de rojo
        imagen_nueva[:,:,1] = prueba_verde  # valores de verde
        imagen_nueva[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(imagen_nueva)

        # Guarda la imagen en un archivo
        imagen_rgb.save("resta.png")
        print("Imagen lista")

        #guarda los vectores del histograma correspondientes a cada canal
        rojo = histograma(m0_tam,matriz0)
        verde = histograma(m1_tam,matriz1)
        azul = histograma(m2_tam,matriz2)

        #une los 3 canales 
        plt.plot(rojo, color='red')
        plt.plot(verde, color='green')
        plt.plot(azul, color='blue')

        plt.show()  #imprime la grafica resultante
        
        plt.imshow(imagen_rgb)
        #ploteo(m0_tam,m1_tam,m2_tam,prueba_rojo,prueba_verde,prueba_azul)
        
    elif opc==3:  # multiplicacion
        val = int(input("Cantidad a multiplicar: "))
        # pruebas para la suma - matrices
        prueba_rojo = multiplicacion(matriz0, f0, c0, val)
        prueba_verde = multiplicacion(matriz1, f1, c1, val)
        prueba_azul = multiplicacion(matriz2, f2, c2, val)

        # histograma de las imagenes
        hist_rojo = histograma(m0_tam, prueba_rojo)
        hist_verde = histograma(m1_tam, prueba_verde)
        hist_azul = histograma(m2_tam, prueba_azul)
        
        imagen_nueva = np.zeros((f,c,3), dtype=np.uint8)
        # Asigna valores a cada canal de color
        imagen_nueva[:,:,0] = prueba_rojo  # valores de rojo
        imagen_nueva[:,:,1] = prueba_verde  # valores de verde
        imagen_nueva[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(imagen_nueva)

        # Guarda la imagen en un archivo
        imagen_rgb.save("multiplicacion.png")
        print("Imagen lista")
        
        #guarda los vectores del histograma correspondientes a cada canal
        rojo = histograma(m0_tam,matriz0)
        verde = histograma(m1_tam,matriz1)
        azul = histograma(m2_tam,matriz2)

        #une los 3 canales 
        plt.plot(rojo, color='red')
        plt.plot(verde, color='green')
        plt.plot(azul, color='blue')

        plt.show()  #imprime la grafica resultante
        plt.imshow(imagen_rgb)
        
        #ploteo(m0_tam,m1_tam,m2_tam,prueba_rojo,prueba_verde,prueba_azul)
        
    elif opc==4:  # division
        val = int(input("Cantidad a dividir: "))
        # pruebas para la suma - matrices
        prueba_rojo = division(matriz0, f0, c0, val)
        prueba_verde = division(matriz1, f1, c1, val)
        prueba_azul = division(matriz2, f2, c2, val)

        # histograma de las imagenes
        hist_rojo = histograma(m0_tam, prueba_rojo)
        hist_verde = histograma(m1_tam, prueba_verde)
        hist_azul = histograma(m2_tam, prueba_azul)
        
        imagen_nueva = np.zeros((f,c,3), dtype=np.uint8)
        # Asigna valores a cada canal de color
        imagen_nueva[:,:,0] = prueba_rojo  # valores de rojo
        imagen_nueva[:,:,1] = prueba_verde  # valores de verde
        imagen_nueva[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(imagen_nueva)

        # Guarda la imagen en un archivo
        imagen_rgb.save("division.png")
        print("Imagen lista")

        #guarda los vectores del histograma correspondientes a cada canal
        rojo = histograma(m0_tam,matriz0)
        verde = histograma(m1_tam,matriz1)
        azul = histograma(m2_tam,matriz2)

        #une los 3 canales 
        plt.plot(rojo, color='red')
        plt.plot(verde, color='green')
        plt.plot(azul, color='blue')

        plt.show()  #imprime la grafica resultante
        plt.imshow(imagen_rgb)
        #ploteo(m0_tam,m1_tam,m2_tam,prueba_rojo,prueba_verde,prueba_azul)
        
    elif opc==5:  # Gamma
        val = int(input("Cantidad a sumar: "))
        # pruebas para la suma - matrices
        prueba_rojo = gamma(matriz0, f0, c0, val)
        prueba_verde = gamma(matriz1, f1, c1, val)
        prueba_azul = gamma(matriz2, f2, c2, val)

        # histograma de las imagenes
        hist_rojo = histograma(m0_tam, prueba_rojo)
        hist_verde = histograma(m1_tam, prueba_verde)
        hist_azul = histograma(m2_tam, prueba_azul)
        
        imagen_nueva = np.zeros((f,c,3), dtype=np.uint8)
        # Asigna valores a cada canal de color
        imagen_nueva[:,:,0] = prueba_rojo  # valores de rojo
        imagen_nueva[:,:,1] = prueba_verde  # valores de verde
        imagen_nueva[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(imagen_nueva)

        # Guarda la imagen en un archivo
        imagen_rgb.save("gamma.png")
        print("Imagen lista")

        #guarda los vectores del histograma correspondientes a cada canal
        rojo = histograma(m0_tam,matriz0)
        verde = histograma(m1_tam,matriz1)
        azul = histograma(m2_tam,matriz2)

        #une los 3 canales 
        plt.plot(rojo, color='red')
        plt.plot(verde, color='green')
        plt.plot(azul, color='blue')

        plt.show()  #imprime la grafica resultante
        plt.imshow(imagen_rgb)
        #ploteo(m0_tam,m1_tam,m2_tam,prueba_rojo,prueba_verde,prueba_azul)
    elif opc==6:  # Inversa
        # pruebas para la suma - matrices
        prueba_rojo = inversa(matriz0, f0, c0)
        prueba_verde = inversa(matriz1, f1, c1)
        prueba_azul = inversa(matriz2, f2, c2)

        # histograma de las imagenes
        hist_rojo = histograma(m0_tam, prueba_rojo)
        hist_verde = histograma(m1_tam, prueba_verde)
        hist_azul = histograma(m2_tam, prueba_azul)
        
        imagen_nueva = np.zeros((f,c,3), dtype=np.uint8)
        # Asigna valores a cada canal de color
        imagen_nueva[:,:,0] = prueba_rojo  # valores de rojo
        imagen_nueva[:,:,1] = prueba_verde  # valores de verde
        imagen_nueva[:,:,2] = prueba_azul  # valores de azul

        # Crea una imagen RGB desde la matriz tridimensional
        imagen_rgb = Image.fromarray(imagen_nueva)

        # Guarda la imagen en un archivo
        imagen_rgb.save("inversa.png")
        print("Imagen lista")

        #guarda los vectores del histograma correspondientes a cada canal
        rojo = histograma(m0_tam,matriz0)
        verde = histograma(m1_tam,matriz1)
        azul = histograma(m2_tam,matriz2)

        #une los 3 canales 
        plt.plot(rojo, color='red')
        plt.plot(verde, color='green')
        plt.plot(azul, color='blue')

        plt.show()  #imprime la grafica resultante
        plt.imshow(imagen_rgb)
        #ploteo(m0_tam,m1_tam,m2_tam,prueba_rojo,prueba_verde,prueba_azul)
    elif opc==6:  # Ecualizacion
        print("Ecualizacion")
    else:
        print("Error. Opcion no valida")
        
    #return opc  #retorna la opcion elegida

menu(matriz_rojo,matriz_verde,matriz_azul, filas, columnas, dimensiones)
ploteo(matriz_rojo,matriz_verde,matriz_azul, filas, columnas)
