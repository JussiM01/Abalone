import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from readdata import *

data = abalone()
data1 = data[['Length', 'Diameter', 'Height', 'Rings']]

sb.pairplot(data1)

plt.show()

data2 = data[['Length', 'Diameter', 'Height', 'Rings', 'Sex']]

sb.pairplot(data2, hue='Sex')

plt.show()

####################

data3 = data[['Length', 'Diameter', 'Height', 'Rings']]

sb.pairplot(data3)

plt.show()

data4 = data[['Length', 'Diameter', 'Height', 'Rings', 'Sex']]

sb.pairplot(data4, hue='Sex')

plt.show()

####################
data1 = data[['Length', 'Diameter', 'Height', 'Rings']]

g = sb.PairGrid(data1)
g.map_diag(sb.kdeplot)
g.map_offdiag(sb.kdeplot, cmap="Blues_d", n_levels=6)

plt.show()

data2 = data[['Length', 'Diameter', 'Height', 'Rings', 'Sex']]

g = sb.PairGrid(data2, hue='Sex')
g.map_diag(sb.kdeplot)
g.map_offdiag(sb.kdeplot, cmap="Blues_d", n_levels=6)

plt.show()
