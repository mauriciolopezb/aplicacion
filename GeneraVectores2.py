# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:39:07 2020

@author: Mauricio Lopez Benitez

Objetivo: Crea un archivo csv a partir de un dataframe que contiene, para todas 
          las posibles combinaciones de programas, 'Id','Pr1' (Programa1),
          'Pr2' (Programa 2), los valores tf-idf de cada trigrama, adicionalmente
          la clase 'Plag' (Etiqueta Reuso de código: Si/No)

"""
import ComparaBolsa as cb 

import pandas as pd
import LeeCsv
import csv

def cargaParejas():
    #
    # Lectura de los datos
    #
    
    M1=[]
    M2=cb.calculaSimilitud()
    M3=[]
    pares=LeeCsv.lectura('../CORPUS/Separacion.csv')
    Mi=[]
    Mj=[]

    #print(pares)
    mTfIdf=cb.calculaFrecuencia() 
       
    #pmTfIdf=pd.DataFrame(mTfIdf)
    #print(pmTfIdf)
    #print(pmTfIdf.loc[0,4575])
    
    for i in range(len(mTfIdf[0])):
        M3.append('NG'+str(i))
    M3.append('Scos')
    M3.append('Plag')    
    M1.append(M3)
    M3=[]
    
        
    for i in range(0,258):
        for ii in range(len(mTfIdf[i])):
                Mi.append(mTfIdf[i][ii])
        for j in range((i+1),259):
          for jj in range(len(mTfIdf[j])):
                Mj.append(mTfIdf[j][jj])
          for r in range(len(Mi)):
              M3.append(abs(Mi[r]-Mj[r]))
          Mj=[]
          M3.append(M2[i][j])
          if ([str(i),str(j)] in pares):
                M3.append(1)
          else:
                M3.append(0)
          M1.append(M3)
          M3=[]
        Mi=[]
    
    csvSalida =open('dataset2.csv','w', newline='')
    salida=csv.writer(csvSalida, delimiter=',')
    
    for fila in M1:
        salida.writerow(fila)
    csvSalida.close()
    
    dataset=pd.DataFrame(M1)
    
         
    # dataset.iloc[:,['Id','Pr1','Pr2','SimCos','Plag']]
    # dataset.head()
    print(dataset)
    return dataset
    
 
    
cargaParejas()