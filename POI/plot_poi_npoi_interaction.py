import matplotlib.pyplot as plt
import sys
import pickle
import sklearn

from data_sorter import featuresProcess
from data_sorter import split

outliers = ["SKILLING JEFFREY K", "LAY KENNETH L", "FREVERT MARK A", "PICKERING MARK R"]

data = pickle.load(open("enron.pkl", "r"))
features = ["salary", "bonus"]
for ii in outliers:
  del data[ii]

def get_information(key, total, data):
  retval = list()
  for ii in data:
    if data[ii][key] == "NaN" or data[ii][total] == "NaN":
      retval.append(0.0)
    elif data[ii][key] >= 0:
      retval.append(float(data[ii][key]) / float(data[ii][total]))
  return retval

email_from_poi = get_information("from_poi_to_this_person", "to_messages", data)

email_to_poi = get_information("from_this_person_to_poi", "from_messages", data)

count = 0
for ii in data:
  data[ii]["email_from_poi"] = email_from_poi[count]
  data[ii]["email_to_poi"] = email_to_poi[count]
  count += 1

features = ["poi", "email_from_poi", "email_to_poi"]
dataset = featuresProcess(data, features)

for ii in dataset:
  from_poi = ii[1]
  to_poi = ii[2]
  if ii[0] == 0:
    plt.scatter(from_poi, to_poi, color = "g")
  if ii[0] == 1:
    plt.scatter(from_poi, to_poi, color = "r", marker = "*")
plt.xlabel("Emails from POIs to Individual")
plt.ylabel("Emails from Individual to POIs")  
plt.savefig("Email % from an Individual to POIs and Non POIs")  
