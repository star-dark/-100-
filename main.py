import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#Dataset 지정
dataset = pd.read_csv('Data.csv') 
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , :3].values
# 평균값에 의해 사라지는 DATA 조정
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[ : , 1:3])
# 범주형 데이터 인코딩
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
# 더미변수 만들기
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
