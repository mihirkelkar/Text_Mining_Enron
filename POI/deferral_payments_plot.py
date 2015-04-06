import pylab
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys

color = list()
payments = list()
data = pickle.load(open("enron.pkl", "r"))
for ii in data.keys():
  if data[ii]['expenses'] != "NaN":
    payments.append(data[ii]['expenses'])
    if data[ii]['poi']:
      color.append('red')
    else:
      color.append('green')
ind = np.arange(len(payments))
fig = pylab.figure()
p1 = plt.bar(ind, payments, color = color)
plt.title("Expenses for Executives")
plt.savefig("Expenses.png", transparent = True)
