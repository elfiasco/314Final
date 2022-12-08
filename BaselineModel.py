import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv('pitches.csv')
test_data = pd.read_csv('hidden.csv')
print(len(train_data))
model = LinearRegression()

X_train = train_data.iloc[:,0:11]
Y_train = train_data.iloc[:,11]
X_test = test_data.iloc[:,0:11]
Y_test = test_data.iloc[:,11]

model.fit(X_train, Y_train)
r_sq = model.score(X_train, Y_train)
print(r_sq)
#print(train_data.dtypes)