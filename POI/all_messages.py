import pylab
import pickle
import matplotlib.pyplot as plt
import numpy as np

data = pickle.load(open("enron.pkl", "r"))
salary = list()
bonus = list()
poi = list()
for ii in data.keys():
  if data[ii]['from_poi_to_this_person'] == 'NaN' or data[ii]['to_messages'] == 'NaN' \
or data[ii]['from_this_person_to_poi'] == "Nan" or data[ii]['from_messages'] == "Nan":
    continue
  else:
    salary.append(data[ii]['from_poi_to_this_person'] + data[ii]['from_this_person_to_poi'])
    bonus.append(data[ii]['to_messages'] + data[ii]['from_messages'])
    if data[ii]['poi']:
      poi.append('red')
    else:
      poi.append('green')
fig = pylab.figure()
salary = np.array(salary) 
bonus = np.array(bonus)
poi = np.array(poi)
plt.scatter(salary, bonus, marker = 'o', color = poi)
plt.xlim(0, 1000)
plt.ylim(0, 20000)
plt.xlabel('All messages between someone charged with crime to Individual')
plt.ylabel('Total Messages sent and recieved by individual')
plt.grid()
plt.savefig('Messages_All.png', transparent = True)   
