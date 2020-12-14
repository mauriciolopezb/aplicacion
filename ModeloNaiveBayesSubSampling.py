# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:08:17 2020

@author: Mauricio Lopez Benitez

Objetivo:  Implementación del modelo Naive-Bayes realizando muestreo por
           SubSampling sobre la clase mayoritaria para estudiar el desbalance
 
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import confusion_matrix

#Clase que permite hacer el subsamplig suprimiendo las observaciones cercanas
from imblearn.under_sampling import NearMiss


from collections import Counter

def modeloNaiveBayesSS():
    
    #Carga del dataset almacenado en csv
    dataset = pd.read_csv('dataset2.csv')
   
   
    #Reducción de la dimensionalidad, con Feature Selection, usando SelctKBest de Sklearn    
    X=dataset.drop(['Plag'], axis=1)
    y=dataset['Plag']
     
    best=SelectKBest(k=50)
    X_new = best.fit_transform(X, y)
    X_new.shape
    selected = best.get_support(indices=True)
    #print(X.columns[selected])
    used_features =X.columns[selected]
    
    # Separación los datos del dataset en los cjtos de entrenamiento y test:
    X_train, X_test = train_test_split(dataset, test_size=0.3, random_state=6) 
    y_train =X_train["Plag"]
    y_test = X_test["Plag"]
    

    #Aplicación del muestreo por subsampling en el cjto de entrenamiento sobre 
    #la clase mayoritaria, reduciendo
    #las observaciones a la misma cantidad de la clase minoritaria
    
    us = NearMiss(sampling_strategy='auto', version=1, n_neighbors=3, n_neighbors_ver3=3, n_jobs=1)
    X_train_res, y_train_res = us.fit_sample(X_train, y_train)
    X_test_res, y_test_res= (X_test, y_test)
     
    # Uso del clasificador Gausiano
    gnb = GaussianNB()
    
    #Con el modelo creado, se utiliza fit() para el aprendizaje
    gnb.fit(
        X_train_res[used_features].values,
        y_train_res
    )
    y_pred = gnb.predict(X_test_res[used_features])
    
    #Calculo de la precisión
     
    print('Precisión en el set de Entrenamiento: {:.2f}'
         .format(gnb.score(X_train_res[used_features], y_train_res)))
    print('Precisión en el set de Test: {:.2f}'
         .format(gnb.score(X_test_res[used_features], y_test_res)))
    
    
    #Calculo de la matriz de confusión
    print(confusion_matrix(y_test_res, y_pred))
    
    print ("Distribución inicial de entrenamiento{}".format(Counter(y_train)))
    print ("Distribución finalde entrenamiento: {}".format(Counter(y_train_res)))
    
    print ("Distribución inicial de test {}".format(Counter(y_test)))
    print ("Distribución final de test: {}".format(Counter(y_test_res)))
    
    
modeloNaiveBayesSS()
    
