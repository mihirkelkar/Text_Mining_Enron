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
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV

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

features_list = ["poi", "salary", "bonus", "email_from_poi", "email_to_poi",'deferral_payments', 'total_payments', 'loan_advances', 'restricted_stock_deferred','deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options',
'long_term_incentive', 'shared_receipt_with_poi', 'restricted_stock', 'director_fees']
dataset = featuresProcess(data, features_list)

labels, features = split(dataset)

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.1, random_state=42)


from sklearn.cross_validation import KFold
kf=KFold(len(labels),3)
for train_indices, test_indices in kf:
    #make training and testing sets
    features_train= [features[ii] for ii in train_indices]
    features_test= [features[ii] for ii in test_indices]
    labels_train=[labels[ii] for ii in train_indices]
    labels_test=[labels[ii] for ii in test_indices]

time_start = time.time()
dtree = DecisionTreeClassifier()
print "Searching the best parameters for the decision tree"
param_grid = {'criterion': ('gini','entropy'),
              'splitter':('best','random'),
              'min_samples_split':[2,3,4,5,6,8],
                'max_features':('auto','sqrt','log2',None),
                'max_depth':[None,1,2,10,50],
                'max_leaf_nodes':[None,2,5,6,7,8,9,10,13]}

dtree = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid)
dtree.fit(features_train, labels_train)
prediction = dtree.predict(features_test)
print dtree.best_estimator_

acc = accuracy_score(labels_test, prediction)
print acc
