import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *
sb.set(style="whitegrid", color_codes="True")

data = abalone()

data_adu = data[data['Sex'] != 'I']

sb.violinplot(x='Rings', y='Diameter', hue='Sex', data=data)

plt.show()

sb.violinplot(x='Rings', y='Diameter', data=data)

plt.show()

sb.violinplot(x='Rings', y='Diameter', data=data_adu, hue='Sex', split=True)

plt.show()

sb.violinplot(x='Rings', y='Diameter', data=data_adu, hue='Sex', split=True, inner='stick', palette='Set3')

plt.show()

sb.violinplot(x='Rings', y='Diameter', data=data_adu, hue='Sex', split=True, inner='stick', palette='Set1')

plt.show()

sb.violinplot(x='Rings', y='Diameter', data=data_adu, hue='Sex', split=True, inner='stick', palette='Set2')

plt.show()
