import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *
sb.set(style="whitegrid", color_codes="True")

data = abalone()

data_adu = data[data['Sex'] != 'I']

sb.pointplot(x='Rings', y='Diameter', hue='Sex', data=data)

plt.show()

sb.pointplot(x='Rings', y='Diameter', hue='Sex', data=data,
    palette={'M': 'g', 'F': 'r', 'I': 'y'}, markers=['^',  'o', 'x'], linestyles=['-','--', '-.'])

plt.show()
