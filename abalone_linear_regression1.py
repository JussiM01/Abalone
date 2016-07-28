from sklearn import linear_model
from readdata import *
from sklearn.metrics import mean_squared_error

X_vars = ['Length', 'Whole Weight']

y_vars = ['Rings']

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)

y_pred = model.predict(X_test)

print('mean squared error of prediction:', mean_squared_error(y_test, y_pred))
