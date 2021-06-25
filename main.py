import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
dataset = pd.read_csv('Data.csv') #Dataset 지정
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , :3].values
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
