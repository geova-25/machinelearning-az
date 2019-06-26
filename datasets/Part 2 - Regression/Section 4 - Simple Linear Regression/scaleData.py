# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:33:20 2019

@author: villagio
"""

from sklearn.preprocessing import StandardScaler 

def scale(X_train, X_test):    
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    return X_train, X_test