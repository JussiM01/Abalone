import matplotlib.pyplot as plt
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
