import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from readdata import *

data = abalone()

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
sb.jointplot(x = 'Length', y = 'Rings', data = data, kind = 'hex', color = 'k')

plt.show()

_, ax = plt.subplots(1)
cmap = sb.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sb.kdeplot(data['Diameter'], data['Rings'], cmap=cmap, n_levels=60, shade=True)

plt.show()
