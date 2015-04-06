import pylab
import pickle
import matplotlib.pyplot as plt
import numpy as np

data = pickle.load(open("enron.pkl", "r"))
salary = list()
bonus = list()
poi = list()
for ii in data.keys():
  if data[ii]['total_stock_value'] == 'NaN' or data[ii]['total_payments'] == 'NaN':
    continue
  else:
    salary.append(data[ii]['total_payments'])
    bonus.append(data[ii]['total_stock_value'])
    if data[ii]['poi']:
      poi.append('red')
    else:
      poi.append('green')
fig = pylab.figure()
salary = np.array(salary) 
bonus = np.array(bonus)
poi = np.array(poi)
plt.scatter(salary, bonus, marker = 'o', color = poi)
plt.xlim(0, 120000000)
plt.ylim(0, 60000000)
plt.xlabel('Payments')
plt.ylabel('Stock Value')
plt.grid()
plt.savefig('Stock_Vs_Payment.png', transparent = True)   
