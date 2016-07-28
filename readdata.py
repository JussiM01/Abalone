import pandas as pd
from sklearn.cross_validation import train_test_split

def abalone():
    data = pd.read_csv('abalone.data', header=None)
    data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight',
                    'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']
    return data

def abalone_train_test():
    data = abalone()
    return train_test_split(data, random_state = 1)
