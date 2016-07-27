import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *
sb.set(style="whitegrid", color_codes="True")

data = abalone()

sb.barplot(x='Rings', y='Diameter', hue='Sex', data=data)

plt.show()

sb.barplot(x='Rings', y='Diameter', data=data, palette='Greens_d')

plt.show()
