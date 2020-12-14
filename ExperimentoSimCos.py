# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:40:57 2020

@author: Mauricio López Benítez


Objetivo: se particiona el dataset en 5 conjuntos (bloques) aleatorios para evaluar 
          el modelo de similitud basada en el coseno.

Esta función recibe: Matriz de similitudes, listaparejas de test,
Lista de parejas de plagio, umbral: se refiere a las medidas de similitud para
realizar las pruebas.

Retorna la tasa de falsos positivos y de verdaderos positivos


"""


import ComparaBolsa as cb 
import LeeCsv
from random import randint


def evaluar(mSimil,lParTest,lParPlag, umbral):
    pos=0
    neg=0
    rpos=0
    fpos=0
    fneg=0
    rneg=0
    for pt in lParTest:
        if (mSimil[pt[0]][pt[1]]) >= umbral:
            if (pt in lParPlag) or (pt[0]==pt[1]):
                rpos +=1
            else:
                fpos +=1
        else:
            if (pt in lParPlag) or (pt[0]==pt[1]):
                fneg +=1
            else:
                rneg +=1
        if pt in lParPlag or (pt[0]==pt[1]):
            pos +=1
        else:
            neg +=1
    print ('Ubral: '+str(umbral)+' Pos: '+str(pos)+' neg: '+str(neg) +
           ' RPos: '+str(rpos)+' Rneg: '+str(rneg) +
           ' FPos: '+str(fpos)+' Fneg: '+str(fneg))
    return ([round((fpos/neg),3),round((rpos/pos),3)])
            



def fsc():
 matriz= cb.calculaSimilitud()
 print("Salida:")
 
 test1=[]
 
 for i in range (0,13561):
     n1=randint(0, 258)
     while True:
         n2=randint(0, 258)
         if (n2>=n1):
             break
     if ([n1,n2] in test1):
         i = i-1
         
     test1.append([n1,n2])
 
 test2=[]
 
 for i in range (0,13416):
     n1=randint(0, 258)
     while True:
         n2=randint(0, 258)
         if (n2>=n1):
             break
     if ([n1,n2] in test2) or ([n1,n2] in test1):
         i = i-1
         
     test2.append([n1,n2]) 

 test3=[]
 
 for i in range (0,13416):
     n1=randint(0, 258)
     while True:
         n2=randint(0, 258)
         if (n2>=n1):
             break
     if ([n1,n2] in test2) or ([n1,n2] in test1) or ([n1,n2] in test3):
         i = i-1
         
     test3.append([n1,n2]) 

 test4=[]
 
 for i in range (0,13416):
     n1=randint(0, 258)
     while True:
         n2=randint(0, 258)
         if (n2>=n1):
             break
     if (([n1,n2] in test2) or ([n1,n2] in test1) or ([n1,n2] in test3) or 
     ([n1,n2] in test4)):
         i = i-1
         
     test4.append([n1,n2]) 

 test5=[]
 
 for i in range (0,13416):
     n1=randint(0, 258)
     while True:
         n2=randint(0, 258)
         if (n2>=n1):
             break
     if (([n1,n2] in test2) or ([n1,n2] in test1) or ([n1,n2] in test3) or 
     ([n1,n2] in test4) or ([n1,n2] in test5)):
         i = i-1
         
     test5.append([n1,n2]) 
     
 pares=LeeCsv.lectura('../CORPUS/Separacion.csv')
 plagios=[]
 for s in pares:
    plagios.append([int(s[0]), int(s[1])])
    
 L1=[] 
 L1.append(evaluar(matriz,test1,plagios, 0.25))
 L1.append(evaluar(matriz,test1,plagios, 0.375))
 L1.append(evaluar(matriz,test1,plagios, 0.5))
 L1.append(evaluar(matriz,test1,plagios, 0.625))
 L1.append(evaluar(matriz,test1,plagios, 0.75))
     
 L2=[] 
 L2.append(evaluar(matriz,test2,plagios, 0.25))
 L2.append(evaluar(matriz,test2,plagios, 0.375))
 L2.append(evaluar(matriz,test2,plagios, 0.5))
 L2.append(evaluar(matriz,test2,plagios, 0.625))
 L2.append(evaluar(matriz,test2,plagios, 0.75))

 L3=[] 
 L3.append(evaluar(matriz,test3,plagios, 0.25))
 L3.append(evaluar(matriz,test3,plagios, 0.375))
 L3.append(evaluar(matriz,test3,plagios, 0.5))
 L3.append(evaluar(matriz,test3,plagios, 0.625))
 L3.append(evaluar(matriz,test3,plagios, 0.75))
 
 L4=[] 
 L4.append(evaluar(matriz,test4,plagios, 0.25))
 L4.append(evaluar(matriz,test4,plagios, 0.375))
 L4.append(evaluar(matriz,test4,plagios, 0.5))
 L4.append(evaluar(matriz,test4,plagios, 0.625))
 L4.append(evaluar(matriz,test4,plagios, 0.75))
 
 L5=[] 
 L5.append(evaluar(matriz,test5,plagios, 0.25))
 L5.append(evaluar(matriz,test5,plagios, 0.375))
 L5.append(evaluar(matriz,test5,plagios, 0.5))
 L5.append(evaluar(matriz,test5,plagios, 0.625))
 L5.append(evaluar(matriz,test5,plagios, 0.75))
 
 print('Bloque 1:')
 print(L1)
 
 print('Bloque 2:')
 print(L2)
 
 print('Bloque 3:')
 print(L3)
 
 print('Bloque 4:')
 print(L4)
 
 print('Bloque 5:')
 print(L5)

fsc()


