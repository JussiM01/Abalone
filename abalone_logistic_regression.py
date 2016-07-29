from sklearn import linear_model
from readdata import *
from sklearn.metrics import accuracy_score
import seaborn as sb
import matplotlib.pyplot as plt

X_vars = ['Length', 'Whole Weight']

y_vars = 'Infant'

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

model = linear_model.LogisticRegression(C=1000000)
model.fit(X_train, y_train)

print(model.coef_)

y_pred = model.predict(X_test)

print('accuracy score of prediction:', accuracy_score(y_test, y_pred))
