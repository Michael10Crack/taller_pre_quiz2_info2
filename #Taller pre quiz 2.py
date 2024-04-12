#Taller pre quiz 2
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import scipy.io as scy

#1 crear la matriz numpy de 4 dim y size 1200000
matriz = np.random.randint(0 , 255, size=(20, 30 , 40 ,50), dtype=np.uint8)

#2 crear la copia de la matriz
copia_matriz = matriz[:,:,0].copy()
#print(copia_matriz)

#3 mostrar atributos 
print(f"""Atributos de la matriz:
    - Dimensiones: {copia_matriz.ndim}
    - Tamaño: {copia_matriz.size}
    - Forma: {copia_matriz.shape}
    - Tipo de dato: {copia_matriz.dtype}
    - Memoria: {copia_matriz.nbytes} bytes
    - Tamaño en bytes de cada elemento: {copia_matriz.itemsize} bytes
    - Elemento de la matriz: {copia_matriz[0, 0, 0]}""")

#4 modificar la forma a 2D
copia_matriz.reshape(10, 3000)
print(f'Tamaño: {copia_matriz.size}')

#5 crear la funcion para convertir la matriz a objeto tipo dataframe de pandas
def matriz_a_dataframe(matriz):
    return pd.DataFrame(matriz)

#6 crear una funcion para cargar .mat y .csv
def cargar_mat(ruta):
    if ruta.endswith('.mat'):
        return scy.loadmat(ruta)
def cargar_csv(ruta):
    if ruta.endswith('.csv'):
        return pd.read_csv(ruta)
    
#7 suma, resta , mult, div, log, prom, desviación estandar 
def Suma(matriz , y=0):
    return np.sum(matriz , axis=y)
def Resta(matriz , y=0):
    return np.subtract(matriz , axis=y)
def Mult(matriz , y=0):
    return np.multiply(matriz , axis=y)
def Div(matriz , y=0):
    return np.divide(matriz , axis=y)
def Log(matriz , y=0):
    return np.log(matriz , axis=y)
def Promedio(matriz , y=0):
    return np.mean(matriz , axis=y)
def Desviacion_estandar(matriz , y=0):
    return np.std(matriz , axis=y)
