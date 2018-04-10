import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


'''
# We also nee to read the cvs file with pandas 'iris.csv'

from
from sklearn.datasets import load_iris
df_iris = load_iris()

or alternatively
df_iris = pd.read_csv('iris.csv')

with the structure of df with petal length of
['setosa', 'versicolor', 'virginica']

we need to define the np array corresponding to versicolor lenght
versicolor_petal_length = df_iris[['versicolor']].values
'''

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
plt.ylabel('ECFD')
plt.xlabel('versicolor petal lenght (cm)')

# Display the plot
plt.show()

# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker = '.', linestyle = 'none')
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
_ = plt.plot(x_virg, y_virg, marker = '.', linestyle = 'none')

# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
