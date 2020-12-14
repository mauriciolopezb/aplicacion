    # -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:08:17 2020

@author: usuario
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.layers import Dropout

def modeloLSTM():
    
    #Carga del dataset almacenado en archivo csv
    #Cada fila contiene la secuencia de una pareja de programas
    #por medio de la representyación numérica de cada trigrama 
    dataset = pd.read_csv('dataset2.csv')
   
  
       
    # Separamción de los datos del dataset en los cjtos de entrenamiento y test:
    X_train, X_test = train_test_split(dataset, test_size=0.2, random_state=6) 
    y_train =X_train["Plag"]
    y_test = X_test["Plag"]


    # creacion del modelo:
    
    #Definición de la capa embedding, se tiene en cuenta la longitud maxima de una secuencia
    
   
    #vector de 32 dimensiones para la incrustración:
    embedding_vecor_length = 32
    max_review_length=500
    
    
    #El modelo sequential se usas como contenedor de la red LSTM
    model = Sequential()
    model.add(Embedding(embedding_vecor_length, input_length=max_review_length))
    
    
    #Definición de un dropout bajo debido al número de neuronas usadas
    model.add(Dropout(0.2))
    
    #Se crea una capa interna de 10 neuronas
    model.add(LSTM(10))
    model.add(Dropout(0.2))
    
    #La función de activación sigmoide permite la clasificación binaria
    model.add(Dense(2, activation='sigmoid'))


    #Uso de adam para optimización
    #Se definen las metricas que se espera calcular
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[tf.keras.metrics.Precision(), 
                                                                         tf.keras.metrics.TruePositives(),
                                                                         tf.keras.metrics.TrueNegatives(),
                                                                         tf.keras.metrics.FalsePositives(),
                                                                         tf.keras.metrics.FalseNegatives(),
                                                                         tf.keras.metrics.Recall() ])
    
    #Entrenamiento del modelo: 
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=64)
 
    # Final evaluacion del modelo

    scores = model.evaluate(X_test, y_test, verbose=0)
    print(model.summary())
    print("Precision: %.2f%%" % (scores[1]*100))
  
    
    #Se imprimen los resultados de las métricas
    print("Scores: ")
    print(scores)
   
    
modeloLSTM()