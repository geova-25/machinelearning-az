
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import categorizeData
import importData
import fixMissingValues
import scaleData


#To divide in test and train set
from sklearn.model_selection import train_test_split

#Import the data
X,y = importData.importDataFromCSV("Salary_Data.csv")

#Change the NaNs
#X = fixMissingValues.changeNaNs(X, np.nan, "mean")

#Categorize non numerical data
#X, y = categorizeData.categorizeData(X, 0, y)

#Split the data between test and train
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2, random_state = 0)

#Scale the data Function
#X_train,X_test = scaleData.scale(X_train, X_test)

#print(X_train)

