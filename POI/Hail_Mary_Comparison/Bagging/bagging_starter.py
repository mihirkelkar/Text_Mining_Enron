import matplotlib.pyplot as plt
import pickle
import numpy as np
import sys

def computeAttribute(convict_messages, messages):
  #Compute fraction attribute given No. of messages with convict/ total
  if messages == "NaN" or messages == "NaNNaN":
    return 0
  elif convict_messages == "NaN" or convict_messages == "NaNNaN":
    return 0
  elif messages == 0:
    return 0
  return float(convict_messages) / float(messages)

def loadDataset():
  data = pickle.load(open('enron.pkl', 'r'))
  outliers = ["FREVERT MARK A", "PICKERING MARK R"]
  for ii in outliers:
    del data[ii]
  return data

def buildFeatures(data):
  for ii in data:
    from_c_to_i = data[ii]['from_poi_to_this_person']
    to_messages = data[ii]['to_messages']
    data[ii]['frac_from_poi'] = computeAttribute(from_c_to_i, to_messages)
    from_i_to_c = data[ii]['from_this_person_to_poi']
    from_messages = data[ii]['from_messages']
    data[ii]['frac_to_poi'] = computeAttribute(from_i_to_c, from_messages) 
    expense = data[ii]['expenses']
    salary = data[ii]['salary']
    data[ii]['expense_per_salary'] = computeAttribute(expense, salary)
    c_all = from_c_to_i + from_i_to_c
    all = to_messages + from_messages
    data[ii]['frac_all'] = computeAttribute(c_all, all)
  return data

def ensemble(data_set, features_list):
  from data_sorter import featuresProcess
  from data_sorter import split
  data = featuresProcess(data_set, features_list)
  labels, features = split(data)
  from sklearn.ensemble import BaggingClassifier
  clf = BaggingClassifier(n_estimators = int(sys.argv[1]), random_state = 202,         bootstrap = True) 
  pickle.dump(clf, open("classifier_ada.pkl", "w"))
  pickle.dump(features_list, open("features_list.pkl", "w"))
  pickle.dump(data_set, open("dataset.pkl", "w"))


def main():
  data_dict = loadDataset()
  data_dict = buildFeatures(data_dict)
  features = ["poi"] + sys.argv[2].split(" ") 
  #"salary", "bonus", "expenses", "exercised_stock_options", "frac_from_poi"]
  #features = ["poi", "frac_from_poi", "frac_to_poi", "shared_receipt_with_poi"]
  ensemble(data_dict, features)

if __name__ == "__main__":
  main()
