
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import categorizeData
import importData
import threatNaN


#To divide in test and train set
from sklearn.model_selection import train_test_split

#Import the data
X,y = importData.importDataFromCSV("Data.csv")

#Change the NaNs
X = threatNaN.changeNaNs(X, np.nan, "mean")

#Categorize non numerical data
X, y = categorizeData.categorizeData(X, 0, y)

#Split the data between test and train
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2, random_state = 0)

print(X_train)

