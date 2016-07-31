from sklearn import ensemble, grid_search
from readdata import *
from sklearn.metrics import accuracy_score
from statplots import *

X_vars = ['Length', 'Whole Weight']

y_vars = 'Infant'

X_train, X_test, y_train, y_test = abalone_train_test(X_vars, y_vars)

param_grid = {'max_depth': list(range(2, 20)),
    'min_samples_split': list(range(2, 20))}


model = ensemble.RandomForestClassifier(n_estimators=100,
    min_samples_split=200, random_state=1)
random_search = grid_search.RandomizedSearchCV(model, param_grid, cv=10,
    scoring='accuracy', n_iter=20, random_state=1)
random_search.fit(X_train, y_train)

print('Scores:', random_search.grid_scores_)
print('Best score:', random_search.best_score_)
print('Best params:', random_search.best_params_)
model = random_search.best_estimator_

y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

print('accuracy score of prediction:', accuracy_score(y_test, y_pred))

confusion_matrix(y_test, y_pred)
roc_curve(y_test, y_pred_proba)
decision_boundary(model, X_test, y_test)
heatmap(model, X_test, y_test)
