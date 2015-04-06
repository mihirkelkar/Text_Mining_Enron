import pylab
import pickle
import matplotlib.pyplot as plt
import numpy as np

data = pickle.load(open("enron.pkl", "r"))
salary = list()
bonus = list()
poi = list()
for ii in data.keys():
  if data[ii]['salary'] == 'NaN' or data[ii]['bonus'] == 'NaN':
    continue
  else:
    salary.append(data[ii]['total_stock_value'])
    bonus.append(data[ii]['exercised_stock_options'])
    if data[ii]['poi']:
      poi.append('red')
    else:
      poi.append('green')
fig = pylab.figure()
salary = np.array(salary) 
bonus = np.array(bonus)
poi = np.array(poi)
plt.scatter(salary, bonus, marker = 'o', color = poi)
plt.xlim(0, 50000000)
plt.ylim(0, 40000000)
plt.xlabel('Total Stocks Owned')
plt.ylabel('Stocks Exercised')
plt.grid()
plt.savefig('total_stock_vs_sale.png', transparent = True)   
