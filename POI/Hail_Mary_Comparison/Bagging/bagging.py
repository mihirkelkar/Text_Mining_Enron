import pickle
from data_sorter import featuresProcess, split
import sys

clf = pickle.load(open('classifier.pkl', 'r'))
data = pickle.load(open('dataset.pkl', 'r'))
features_list = pickle.load(open('features_list.pkl', 'r'))

data = featuresProcess(data, features_list)
labels, features = split(data)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.cross_validation import StratifiedKFold

precision = 0
accuracy = 0
recall = 0
for counter in range(0, 10):
  folded = StratifiedKFold(labels, n_folds = int(sys.argv[1]), shuffle = True)
  for train_instance , test_instance in folded:
    features_train = list()
    features_test = list()
    labels_train = list()
    labels_test = list()
    for ii in train_instance:
      features_train.append(features[ii])
      labels_train.append(labels[ii])
    for jj in test_instance:
      features_test.append(features[jj])
      labels_test.append(labels[jj])
  
    clf.fit(features_train, labels_train)
    prediction = clf.predict(features_test)
    score = clf.score(features_test, labels_test)
    #print "Accuracy score : %s" %score
    #print "Precision score : %s" %(precision_score(labels_test, prediction))
    #print "Recall_Score : %s" %(recall_score(labels_test, prediction))
    precision += precision_score(labels_test, prediction)  
    recall += recall_score(labels_test, prediction)
    accuracy += score

divider = 10.0 * int(sys.argv[1])
precision = float(precision) / float(divider)
recall = float(recall) / float(divider)
accuracy = float(accuracy) / float(divider)
if precision != 0.0 and recall != 0.0:
  f = float(2 * precision * recall) / float(precision + recall)
else:
  f = "undefined"
fp  = open('Result/Result', 'a')
fp.write("Features are %s\n" %sys.argv[3])
fp.write("Algrithm : Aggregate Boosting\n")
fp.write("Number of Estimators : %s\n" %sys.argv[2])
fp.write("Folds for cross validation : %s\n" % str(sys.argv[1]))
fp.write("Precision : %s\n" % str(precision))
fp.write("Recall : %s\n" % str(recall))
fp.write("Accuracy : %s\n" % str(accuracy))
fp.write("F-Meaure : %s\n" % str(f))
fp.write("- - - - - - - - - - - - - - \n")
fp.close()
