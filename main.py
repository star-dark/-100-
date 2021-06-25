import numpy as np
import pandas as pd
dataset = pd.read_csv('Data.csv') #Dataset 지정
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , :3].values
