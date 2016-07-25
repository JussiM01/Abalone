import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('abalone.data', header=None)
data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Height',
                'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']

_, ax = plt.subplots(4, 2)
sb.distplot(data['Length'], axlabel = 'Length', ax = ax[0][0])
sb.distplot(data['Diameter'], axlabel = 'Diameter', ax = ax[0][1])
sb.distplot(data['Height'], axlabel = 'Height', ax = ax[1][0])
sb.distplot(data['Whole Height'], axlabel = 'Whole Height', ax = ax[1][1])
sb.distplot(data['Shucked Weight'], axlabel = 'Shucked Weight', ax = ax[2][0])
sb.distplot(data['Viscera Weight'], axlabel = 'Viscera Weight', ax = ax[2][1])
sb.distplot(data['Shell Weight'], axlabel = 'Shell Weight', ax = ax[3][0])
sb.distplot(data['Rings'], axlabel = 'Rings', ax = ax[3][1])

_, ax = plt.subplots(1)

sb.countplot(x = 'Sex', data = data, ax = ax)

sb.jointplot(x = 'Length', y = 'Diameter', data = data)

plt.show()
