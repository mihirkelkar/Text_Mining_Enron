import pickle
from data_sorter import featuresProcess, split
import sys

clf = pickle.load(open('classifier_ada.pkl', 'r'))
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
  folded = StratifiedKFold(labels, n_folds = 10)
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
    print "Accuracy score : %s" %score
    print "Precision score : %s" %(precision_score(labels_test, prediction))
    print "Recall_Score : %s" %(recall_score(labels_test, prediction))
    precision += precision_score(labels_test, prediction)  
    recall += recall_score(labels_test, prediction)
    accuracy += score

fp  = open('Graph/Ada_Boost_Optimal_performace', 'w')
fp.write("Learning Rate : %s, Iterators : %s, Precision : %s, Recall %s, Accuracy :%s \n" %(sys.argv[2], sys.argv[1], float(precision)/100.0, float(recall) / 100.0, float(accuracy) / 100.0 ))
fp.close()

