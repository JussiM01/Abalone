import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *

sb.set(color_codes=True)

data = abalone()
data_conv = data[['Length', 'Diameter', 'Height', 'Whole Weight',
    'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']].astype('float64')

sb.regplot(x='Length', y='Diameter', data=data_conv)

sb.lmplot(x='Rings', y='Length', data=data_conv, x_estimator=np.mean)

sb.lmplot(x='Rings', y='Shell Weight', data=data_conv, x_estimator=np.mean)

sb.lmplot(x='Rings', y='Whole Weight', data=data_conv, x_estimator=np.mean)

plt.show()
