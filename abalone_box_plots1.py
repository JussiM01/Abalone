import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *
sb.set(style="whitegrid", color_codes="True")

data = abalone()

_, ax = plt.subplots(1)

sb.boxplot(x='Rings', y='Diameter', data=data, ax=ax)

_, ax = plt.subplots(1)

sb.boxplot(x='Rings', y='Diameter', hue='Sex', data=data, ax=ax)

plt.show()
