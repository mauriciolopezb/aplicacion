# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:08:17 2020

@author: Mauricio Lopez Benitez

Objetivo:  Implementar el modelo Naive-Bayes sin manejo del desbalance de las 
           clases, con manejo de la reducción de dimensionalidad

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import confusion_matrix




def modeloNaiveBayes():
    
    #Carga de los vectores del dataset almacenado en csv
    dataset = pd.read_csv('dataset2.csv')
   
    
   

    #Reducción de la dimensionalidad, con Feature Selection, 
    #usando SelctKBest de Sklearn    
    
    X=dataset.drop(['Plag'], axis=1)
    y=dataset['Plag']
     
    best=SelectKBest(k=50)
    X_new = best.fit_transform(X, y)
    X_new.shape
    selected = best.get_support(indices=True)
    
    
    #print(X.columns[selected])
    used_features =X.columns[selected]
    
    # Separación de los datos del dataset en los cjtos de entrenamiento y test:
    X_train, X_test = train_test_split(dataset, test_size=0.3, random_state=6) 
    
    #Se separa el astributo clase 
    y_train =X_train["Plag"]
    y_test = X_test["Plag"]
    
    
     
     
    #Uso del clasificador Gausiano    
    gnb = GaussianNB()
    
    #Con el modelo creado, se utiliza fit() para el aprendizaje
    gnb.fit(
        X_train[used_features].values,
        y_train
    )
    y_pred = gnb.predict(X_test[used_features])
    
    #Calculo de la precisión
     
    print('Precisión en el set de Entrenamiento: {:.2f}'
         .format(gnb.score(X_train[used_features], y_train)))
    print('Precisión en el set de Test: {:.2f}'
         .format(gnb.score(X_test[used_features], y_test)))
    
    
    #Calculo de la matriz de confusión
    print(confusion_matrix(y_test, y_pred))
    
    print('Valores del dataset: ')
    print(X_new.shape)
    print(pd.value_counts(dataset['Plag'], sort = True))

modeloNaiveBayes()
    
