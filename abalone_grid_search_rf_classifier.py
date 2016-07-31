from sklearn import ensemble, grid_search
from readdata import *
from sklearn.metrics import accuracy_score
from statplots import *

X_vars = ['Length', 'Whole Weight']

y_vars = 'Infant'

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

param_grid = {'max_depth': list(range(2, 20))}


model = ensemble.RandomForestClassifier(n_estimators=100,
    min_samples_split=200, random_state=1)
grid = grid_search.GridSearchCV(model, param_grid, cv=10, scoring='accuracy')
grid.fit(X_train, y_train)

print('Scores:', grid.grid_scores_)
print('Best score:', grid.best_score_)
print('Best params:', grid.best_params_)
model = grid.best_estimator_

y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

print('accuracy score of prediction:', accuracy_score(y_test, y_pred))

confusion_matrix(y_test, y_pred)
roc_curve(y_test, y_pred_proba)
decision_boundary(model, X_test, y_test)
heatmap(model, X_test, y_test)
