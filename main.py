import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
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
# DATA SET을 훈련용 DATA와 시험용 DATA로 나누기
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
# 데이터 스케일링 (표준 스케일링)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
