import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *

sb.set(color_codes=True)

data = abalone()

sb.jointplot(x='Rings', y='Whole Weight', data=data, kind='reg')

plt.show()
