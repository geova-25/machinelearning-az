#To threat NA
from sklearn.impute import SimpleImputer

def changeNaNs(X,mss_vls,strgy):
    imputer = SimpleImputer(missing_values = mss_vls, strategy = strgy)
    #The last values is not taken into account so had to put 3 instead of two to
    #use 1 and 3
    imputer = imputer.fit(X[:,1:3])
    X[:,1:3] = imputer.transform(X[:,1:3])
    return X