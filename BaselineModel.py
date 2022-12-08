import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv('pitches.csv')
test_data = pd.read_csv('hidden.csv')
model = LinearRegression()

Y_test = test_data.iloc[:,11]
baseline_pred = np.zeros(Y_test.shape)

def score(pred):
    dif = (Y_test - pred)**2
    return(np.mean(dif))

test0 = score(baseline_pred)
print(test0)