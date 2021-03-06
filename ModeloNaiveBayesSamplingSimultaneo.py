# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:08:17 2020

@author: usuario
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import confusion_matrix

from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline

from collections import Counter

def modeloNaiveBayesSampling():
    
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
    
    # Separación de los datos del dataset en los cjtos de entrenamiento y test:
    X_train, X_test = train_test_split(dataset, test_size=0.3, random_state=6) 
    y_train =X_train["Plag"]
    y_test = X_test["Plag"]
    
	
    #Configuración del muestreo que combina oversampling y subsamplig:
    os = make_pipeline(
    SMOTE(sampling_strategy={1: 5000}),
    NearMiss(sampling_strategy={0: 15000}))


    X_train_res, y_train_res = os.fit_resample(X_train, y_train)
  
    X_test_res, y_test_res= (X_test, y_test)
     
    
    # Uso del clasificador Gausiano:
    gnb = GaussianNB()
    
    
    #Con el modelo creado, se utiliza fit() para el aprendizaje
    gnb.fit(
        X_train_res[used_features].values,
        y_train_res
    )
    y_pred = gnb.predict(X_test_res[used_features])
    
    #Calculamos la precisión
     
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
    

modeloNaiveBayesSampling()
    
