# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:54:18 2020

@author: Mauricio López

Objetivo: Lee los archivos del corpus de datos, separa las cadenas en una lista,
          agrega la lista de cadenas de cada programa a la lista fuentes
          que contendrá todas las listas del corpus

Salida: Lista fuentes.
"""


def cargarDatos():
        
       fuentes=[]      
       for f in range(0,259):
                     
        if (f<10):
            fuente='../CORPUS/java/00'+str(f)+'.java'
        elif (f<100):
            fuente='../CORPUS/java/0'+str(f)+'.java'
        else:
           
            fuente='../CORPUS/java/'+str(f)+'.java'    
        
        archivo_texto = open(fuente, "r")
        
        texto = archivo_texto.read()
        archivo_texto.close()
        
        palabras = texto.split()
        
        fuentes.append(palabras)
        
       
        #print("Longitudes archivo:   "+str(f)+" es "+ str(len(fuentes[f])))
       return fuentes
        
cargarDatos()