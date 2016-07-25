import pandas as pd

def abalone():
    data = pd.read_csv('abalone.data', header=None)
    data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Height',
                    'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']
    return data
