import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import pickle
import numpy as np
import pylab
from data_sorter import split
from data_sorter import featuresProcess

datadict = pickle.load(open("enron.pkl", "r"))
features = ["salary", "bonus", "total_stock_value"]
data = featuresProcess(datadict, features)
temp_list = list()
for ii in data:
  temp_list.append((ii[0], ii[1], ii[1]))
temp_list = sorted(temp_list, key = lambda x : x[0], reverse = True)
for ii in range(4):
  temp_list.pop(0)
fig = pylab.figure()
ax = Axes3D(fig)
ax.scatter([ii[0] for ii in  temp_list], [ii[1] for ii in temp_list], [ii[2] for ii in temp_list])
plt.xlabel('Salaries')
plt.ylabel('Bonus')
ax.set_zlabel('Stocks')
plt.savefig("Enron Salalries No Outliers 3d")

