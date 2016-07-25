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
