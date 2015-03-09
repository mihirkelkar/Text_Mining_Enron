import matplotlib.pyplot as plt
import sys
import pickle
import sklearn
import time
import numpy as np

from data_sorter import featuresProcess
from data_sorter import split
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier

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




features_list = ["poi", "salary", "email_from_poi", "email_to_poi",'deferral_payments', 'total_payments']

dataset = featuresProcess(data, features_list)

labels, features = split(dataset)
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.1, random_state=42)

time_start = time.time()

dtree = DecisionTreeClassifier()
dtree.fit(features_train, labels_train)
score = dtree.score(features_test, labels_test)
print "Accuracy ", score

print "Decesion tree took time : ", time.time() - time_start

feat_ranks = dtree.feature_importances_
indices = np.argsort(feat_ranks)[::-1]
for ii in range(4):
  print "{} feature {} ({})".format(ii+1, features_list[ii + 1], feat_ranks[indices[ii]])

