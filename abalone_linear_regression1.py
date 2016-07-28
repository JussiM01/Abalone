from sklearn import linear_model
from readdata import *

X_vars = ['Length', 'Whole Weight']

y_vars = ['Rings']

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)
