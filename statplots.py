import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics

def confusion_matrix(y_test, y_pred):
    cm = metrics.confusion_matrix(y_test, y_pred)
    print('Confusion matrix:')
    print(cm)
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.colorbar()
    plt.xticks([0, 1], [0, 1])
    plt.yticks([0, 1], [0, 1])
    plt.xlabel('Prediction')
    plt.ylabel('Test')
    plt.show()

def roc_curve(y_test, y_pred_proba):
    print('Area under curve:')
    print(metrics.roc_auc_score(y_test, y_pred_proba[:,1]))
    fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_proba[:,1])
    plt.figure()
    plt.plot(fpr, tpr)
    plt.show()

def decision_boundary(model, X_test, y_test, grid_size=200):
    X_test = X_test.values
    xmin, xmax = X_test[:, 0].min(), X_test[:, 0].max()
    ymin, ymax = X_test[:, 1].min(), X_test[:, 1].max()
    xstep, ystep = (xmax -xmin)/grid_size, (ymax -ymin)/grid_size
    xr = np.arange(xmin, xmax, xstep)
    yr = np.arange(ymin, ymax, ystep)
    xgrid, ygrid =  np.meshgrid(xr, yr)
    pred = model.predict(np.c_[xgrid.ravel(), ygrid.ravel()]).reshape(xgrid.shape)
    plt.figure()
    plt.contourf(xgrid, ygrid, pred)
    rows0 = np.where(y_test == 0)
    rows1 = np.where(y_test == 1)
    plt.scatter(X_test[rows0, 0], X_test[rows0, 1], color='k', s=1)
    plt.scatter(X_test[rows1, 0], X_test[rows1, 1], color='w', s=1)
    plt.show()

def heatmap(model, X_test, y_test, grid_size=200):
    X_test = X_test.values
    xmin, xmax = X_test[:, 0].min(), X_test[:, 0].max()
    ymin, ymax = X_test[:, 1].min(), X_test[:, 1].max()
    xstep, ystep = (xmax -xmin)/grid_size, (ymax -ymin)/grid_size
    xr = np.arange(xmin, xmax, xstep)
    yr = np.arange(ymin, ymax, ystep)
    xgrid, ygrid =  np.meshgrid(xr, yr)
    pred = model.predict_proba(np.c_[xgrid.ravel(), ygrid.ravel()])[:,1].reshape(xgrid.shape)
    plt.figure()
    plt.pcolormesh(xgrid, ygrid, pred)
    plt.colorbar()
    rows0 = np.where(y_test == 0)
    rows1 = np.where(y_test == 1)
    plt.scatter(X_test[rows0, 0], X_test[rows0, 1], color='k', s=1)
    plt.scatter(X_test[rows1, 0], X_test[rows1, 1], color='w', s=1)
    plt.show()
