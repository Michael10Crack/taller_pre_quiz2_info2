#Taller pre quiz 2
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#1 crear la matriz numpy de 4 dim y size 1200000
matriz = np.random.randint(0 , 255, size=(20, 30 , 40 ,50), dtype=np.uint8)

#2 crear la copia de la matriz
copia_matriz = matriz[:,:,0].copy()
#print(copia_matriz)

#3 mostrar atributos 
