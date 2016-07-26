import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
from readdata import *

sb.set(color_codes=True)

data = abalone()

sb.pairplot(data, x_vars=['Whole Weight', 'Shucked Weight', 'Viscera Weight',
    'Shell Weight'], y_vars=['Rings'], size=5, hue='Sex', kind='reg')

plt.show()
