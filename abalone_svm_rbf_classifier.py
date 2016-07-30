from sklearn import svm
from readdata import *
from sklearn.metrics import accuracy_score
from statplots import *

X_vars = ['Length', 'Whole Weight']

y_vars = 'Infant'

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

model = svm.SVC(kernel='rbf', gamma=10, C=10)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('accuracy score of prediction:', accuracy_score(y_test, y_pred))

confusion_matrix(y_test, y_pred)
decision_boundary(model, X_test, y_test)
