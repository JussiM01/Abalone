import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *

sb.set(color_codes=True)

data = abalone()

sb.lmplot(x='Rings', y='Whole Weight', data=data, x_estimator=np.mean, hue='Sex')

sb.lmplot(x='Rings', y='Whole Weight', data=data, x_estimator=np.mean, col='Sex')

plt.show()
