# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:53:30 2020

@author: Mauricio Lopez Benitez

Objetivo: Implementar el modelo de similitud coseno basado en la idea de
la bolsa de palabras.

Salida: similitud coseno para cada pareja de códigos fuente.
"""

import ConverToken as convierte

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity




#  Función para calcular la frecuencia de término de los trigramas en 
#  la lista de trigramas de cada código fuente

def calculaTF(frecuenciaPalabra, fuentePalabra):
    tfDict = {}
    bagOfWordsCount = len(fuentePalabra)
    if bagOfWordsCount==0:
        print(fuentePalabra)
    for word, count in frecuenciaPalabra.items():
         tfDict[word] = count / float (bagOfWordsCount)
    return tfDict


#Cálculo de la frecuencia inversa de término

def calculaIDF(documento):
    import math
    N = len(documento)
    
    idfDict = dict.fromkeys(documento[0].keys(), 0)
    for document in documento:
        for palabra, val in document.items():
            if val > 0:
                idfDict[palabra] += 1
    
    for palabra, val in idfDict.items():
        idfDict[palabra] = math.log(N / float(val))
    return idfDict


#Cálculo de la frecuencia inversa de término-frecuencia inversa de documento
def calculaTFIDF(tfPalabras, idfT):
    tfidf = {}
    for palabra, val in tfPalabras.items():
        tfidf[palabra] = val * idfT[palabra]
    return tfidf


#Cálculo de la frecuencia de cada trigrama en el documento. (Archivo fuente)
def calculaFrecuencia():
  
   fuentes=[]   
   palabrasUnicas=[]
   frecuencias=[]
   tf=[]
   mTfIdf=[]
    

    #Genero una lista de n-gramas de token de cada archivo a la vez:    
    #cada lista de n-gramas de token se agrega al conjunto de fuentes
    
   fuentes=convierte.nGramaToken()
 
    

   palabrasUnicas=[]   
   
   #Identificamos los n-gramas de token diferentes entre los archivos
   
   for fuente in fuentes:
       palabrasUnicas = set(palabrasUnicas).union(set(fuente))
        
       
   #Creamos un diccionario para contabilizar la frecuencia de las palabras 
   
   for i in fuentes:
       frecuenciaPalabra = dict.fromkeys(palabrasUnicas,0)
       for word in i:
            frecuenciaPalabra[word] += 1
            
       #Creo una lista de diccionarios para agregar las frecuencias de cada fuente
       frecuencias.append(frecuenciaPalabra)

       #Calculo la frecuencia de términos para cada archivo fuente
       #print("Archivo "+ str(i))
       
       #  print("A"+str(i) + " Len: " + str(len(fuentes[i] )))
       tf.append(calculaTF(frecuenciaPalabra, i))
                               
   idfTotal=calculaIDF(frecuencias)
    
   #Calcular TF-IDF para los documentos:
   
   for i in tf:
        tfidf=(calculaTFIDF(i, idfTotal))
        vTfidf=[]              
        for clave in tfidf:
            vTfidf.append(tfidf[clave])
        mTfIdf.append(vTfidf)
   return mTfIdf



#Estimación de la similitud coseno de cada pareja de códigos.
   
def calculaSimilitud():
   
   mTfIdf=calculaFrecuencia() 
      
   df = pd.DataFrame(mTfIdf)
    
        
   simil1=cosine_similarity(df,df)
        
   #print (simil1)
   return simil1
   
    
    