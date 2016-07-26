import numpy as
import pandas as import pd
import matplolib as mpl
import seaborn as sb
from readdata import *

sb.set(color_codes=True)

data = abalone()

sb.regplot(x='Length', y='Diameter', data=data)

plt.show()
