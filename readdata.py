import pandas as pd
from sklearn.cross_validation import train_test_split

def abalone():
    data = pd.read_csv('abalone.data', header=None)
    data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight',
                    'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']
    return data

def abalone_train_test(X_vars, y_vars):
    data = abalone()
    X = data[X_vars]
    y = data[y_vars]
    return train_test_split(X, y, random_state = 1)
