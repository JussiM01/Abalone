from sklearn import ensemble
from readdata import *
from sklearn.metrics import mean_squared_error
import seaborn as sb
import matplotlib.pyplot as plt

X_vars = ['Length', 'Whole Weight']

y_vars = ['Rings']

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

model = ensemble.RandomForestRegressor(n_estimators=100, max_depth=4, random_state=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('mean squared error of prediction:', mean_squared_error(y_test, y_pred))

comparison = y_test.copy()
comparison['Prediction'] = y_pred

sb.jointplot(x = 'Rings', y = 'Prediction', xlim=(0,25), ylim=(0,25), data=comparison)

plt.show()
