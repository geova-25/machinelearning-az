# -*- coding: utf-8 -*-

import pandas as pd

#This function assumes that reads everything except the last column
def importDataFromCSV(fileName):
    #Read the csv file
    dataset = pd.read_csv(fileName)    
    #Here the import of the data is made, X is the independant data matrix
    X = dataset.iloc[:,:-1].values
    #y is the dependand data vector
    y = dataset.iloc[:,-1].values
    return X, y

