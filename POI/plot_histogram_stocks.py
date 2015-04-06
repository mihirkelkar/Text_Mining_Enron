import pylab
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys

total_stock_value = list()
sold_stock = list()
poi = list()
data = pickle.load(open("enron.pkl", "r"))
for ii in data.keys():
  if data[ii]['total_stock_value'] == "NaN" or data[ii]['exercised_stock_options'] == "NaN":
    continue
  else:
    if data[ii]['poi']:
      total_stock_value.append(data[ii]['total_stock_value'])
      sold_stock.append(data[ii]['exercised_stock_options'])
      poi.append(data[ii]['poi'])

poi_list = list()
for ii in poi:
  if ii:
    poi_list.append("*")
  else:
    poi_list.append("")
print poi
N = len(total_stock_value)
ind = np.arange(N)
fig = pylab.figure()
p1 = plt.bar(ind, total_stock_value, color = 'blue')
p2 = plt.bar(ind, sold_stock, color = 'black')
plt.title("Amount of stock owned and exercised per person")
#plt.xticks(poi_list)
plt.legend((p1[0], p2[0]), ('Total Stock', 'Exercised Stock'))
plt.savefig('StockOwn_Hist.png', transparent = True) 
