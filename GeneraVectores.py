# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:39:07 2020

@author: Mauricio Lopez Benitez

Objetivo: Crea un archivo csv con la representación numérica de la secuencia de 
          trigramas de token, por pares de código y su respectiva clase.

"""

import ConverToken as convierte


import pandas as pd
import LeeCsv
import csv


def codificarTrigramas():
    
   fuentes=convierte.nGramaToken()   
 
   palabrasUnicas=[]   
   
   #Identificamos los n-gramas de token diferentes entre los archivos
   
   for fuente in fuentes:
       palabrasUnicas = set(palabrasUnicas).union(set(fuente))
   
   codTG = dict.fromkeys(palabrasUnicas,0)     
   
   i=1
   for k in codTG:
       codTG[k]=i
       i = i+1
   
   
   listaTG=[]
   dataSetTG=[]
   for fuente in fuentes:
       for j in fuente:
           listaTG.append(codTG[j])
       dataSetTG.append(listaTG)
       listaTG=[]
       
   return dataSetTG
       
       
        
def cargaParejas():
    #
    # Lectura de los datos
    #
    
    M1=[]
    M2=codificarTrigramas()
    M3=[]
    pares=LeeCsv.lectura('../CORPUS/Separacion.csv')
       
       
    for i in range(0,258):
        for ii in range(len(M2[i])):
                M3.append(M2[i][ii])
        for j in range((i+1),259):
          for jj in range(len(M2[j])):
                M3.append(M2[j][jj])
         
          if ([str(i),str(j)] in pares):
                M3.append(1)
          else:
                M3.append(0)
          M1.append(M3)
          M3=[]
 
    
    csvSalida =open('dataset.csv','w', newline='')
    salida=csv.writer(csvSalida, delimiter=',')
    
    for fila in M1:
        salida.writerow(fila)
    csvSalida.close()
    
    dataset=pd.DataFrame(M1)
    
    print(dataset)
    return dataset
    
 
    
cargaParejas()