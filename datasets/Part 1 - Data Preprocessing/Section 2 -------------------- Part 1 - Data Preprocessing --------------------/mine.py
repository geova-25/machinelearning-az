
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#To threat NA
from sklearn.impute import SimpleImputer
#To threat non numerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#To select just a column
from sklearn.compose import ColumnTransformer
#To divide in test and train set
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Data.csv')
#Toma todas las filas y columnas excepto la ultima columna, se hace con el -1
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#NaN con mayuscula funciona de igual manera, Axis = 0 significa columna, 1 es fil a
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
#The last values is not taken into account so had to put 3 instead of two to
#use 1 and 3
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#Modifying categoric data
#Transform String into NumericValues

#labelEncoder_X = LabelEncoder()
#X[:,0] = labelEncoder_X.fit_transform(X[:,0])
#Transform Numeric values into encoder binary values

oneHotEncoder = ColumnTransformer(
    transformers=[
        ("OneHot",        # Just a name
         OneHotEncoder(), # The transformer class
         [0]              # The column(s) to be applied on.
         )
    ]
)

X = np.hstack((oneHotEncoder.fit_transform(X),X[:,1:]))
#X = oneHotEncoder.fit_transform(X)
#Para los datos de y
labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y)
#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2, random_state = 0)
print(X_train)
