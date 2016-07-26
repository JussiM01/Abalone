import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from readdata import *

data = abalone()


data1 = data[['Length', 'Diameter', 'Height', 'Whole Weight']]

sb.pairplot(data1, diag_kind='kde')

plt.show()

data2 = data[['Length', 'Diameter', 'Height', 'Whole Weight', 'Sex']]

sb.pairplot(data2, diag_kind='kde', hue='Sex')

plt.show()
