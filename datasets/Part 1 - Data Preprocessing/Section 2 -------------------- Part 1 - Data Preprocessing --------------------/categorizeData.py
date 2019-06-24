import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#Function for definying a clasification not a range of values
def categorizeData(X, col, y ):
    oneHotEncoder = ColumnTransformer(
        transformers=[
            ("OneHot",        # Just a name
             OneHotEncoder(), # The transformer class
             [col]              # The column(s) to be applied on.
             )
        ]
    )
    
    X = np.hstack((oneHotEncoder.fit_transform(X),X[:,1:]))
    #X = oneHotEncoder.fit_transform(X)
    #For the y data we use Label encoder
    labelEncoder_Y = LabelEncoder()
    y = labelEncoder_Y.fit_transform(y)
    return X, y
