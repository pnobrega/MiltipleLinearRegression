# -*- coding: utf-8 -*-
"""MultLinearRegres.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ov4xyhV-kW5c8320P1X378ktkaMSx5gQ
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_profiling

url = 'https://raw.githubusercontent.com/pnobrega/MiltipleLinearRegression/master/50_Startups.csv'

# Importing the dataset
dataset = pd.read_csv(url)

pandas_profiling.ProfileReport(dataset)

dataset.head()

dataset.tail()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Droping the dummy variable (fist column)
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fit mutiple linear regression to the train test
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

y_pred

y_test

import matplotlib.pyplot as plt
# Data for plotting
plt.plot(y_pred)
plt.ylabel("Predict")
plt.show()

plt.plot(y_test)
plt.ylabel("Test")
plt.show()
