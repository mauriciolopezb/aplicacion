# -*- coding: utf-8 -*-


""" 
@author: Mauricio Lopez Benitez 

Objetivo:
Recibe las cadenas leidas en cada archivo fuente y genera una lista con las 
palabras y símbolos   identificados

"""

import cargaCorpus

#Verifica si una cadena es un número

def identificaNum(cadena):
   try:
       float(cadena)
       return True
   except (TypeError, ValueError):
       return False
   
def identificaNumHexa(cadena):
    try:
        int(cadena,16)
        return True
    except (TypeError, ValueError):
        return False



#Función para separar simbolos y caracterres especiales de cada palabra (cadena)
#Devuelve la lista Retorno, con las cadenas y simbolos separados.


def separarSimbolos (cadena):
    textoAbierto=False
    retorno =[]
    #print("\nEntra: "+cadena)
    
    nuevaCadena = ""
    cadenaSimbolo=""
    
    if identificaNum(cadena):
        retorno.append('numero')
        return retorno
    
    if identificaNumHexa(cadena):
       retorno.append('numeroHx')
       return retorno
        
    for j in cadena:       
        if (j=='"'):
            if (textoAbierto):
                textoAbierto =False
                retorno.append('texto')
            else:
                textoAbierto=True
                if (cadenaSimbolo !=""):
                     retorno.append(cadenaSimbolo)
                     cadenaSimbolo=""
            continue
        
        if  (j==';'):
            continue
        if ( ((j=='{') or (j=='(') or (j=='[') or (j=='}') or (j==')') or (j==']')
            or (j=='+') or (j=='-') or (j=='*') or (j=='/') 
            or (j=='%') or (j=='=') or (j=='!')  or (j=='&') or (j=='|')
            or (j=='>') or (j=='<') or (j==',') or (j=='\\') )):
            if (nuevaCadena!="" and textoAbierto==False):
                 if identificaNum(nuevaCadena):
                     retorno.append('numero')
                 elif identificaNumHexa(nuevaCadena):
                     retorno.append('numeroHx')
                 else:
                     retorno.append(nuevaCadena)
                 cadenaSimbolo = cadenaSimbolo + j
            else: 
                if (textoAbierto==False):
                    if(".{([])}".find(j) == -1):
                        cadenaSimbolo = cadenaSimbolo +j
                    else:
                        retorno.append(j)
                    
            nuevaCadena=""
        else:
            if (cadenaSimbolo !=""):
                retorno.append(cadenaSimbolo)
                cadenaSimbolo=""
            nuevaCadena= nuevaCadena+j
    if (textoAbierto==False):
        if (nuevaCadena!=""):
            if (identificaNum(nuevaCadena)):
                retorno.append('numero')
            else:
                retorno.append(nuevaCadena)
        if (cadenaSimbolo != ""):
            retorno.append(cadenaSimbolo)
    return retorno


#Identifica las cadenas en el archivo de entrada:

def identificarPalabras():

      salida=[]
      
      fuentes = cargaCorpus.cargarDatos()


#Retorna en la lista cadenas todas las cadenas y simbolos separados.
      for palabras in fuentes:
        cadenas= []

        for i in palabras:
            cadenaTempo = separarSimbolos(i)
            for k in cadenaTempo:
                cadenas.append(k)
        salida.append(cadenas)
       
      return salida
    
#identificarPalabras()

    

        
        
        
        