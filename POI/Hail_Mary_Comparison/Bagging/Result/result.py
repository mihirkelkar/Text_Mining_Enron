import matplotlib.pyplot as plt
"""
Reading the data into a list so that we could pivot it. 
"""
import sys
fp = open('Result', 'r')
total_file = list()
temp_dict = {}
for line in fp:
  line = line.strip()
  if line.strip() == "- - - - - - - - - - - - - -":
    total_file.append(temp_dict)
    temp_dict = {}
    continue
  else:
    index, value = line.split(":")
    index = index.strip()
    if index == "Algrithm":
      pass
    elif index == "Number of Estimators":
      temp_dict['num'] = float(value)
    elif index == "Folds for cross validation":
      temp_dict['fold'] = float(value)
    elif index == "Precision":
      temp_dict['pre'] = float(value)
    elif index == "Recall":
      temp_dict['recall'] = float(value)
    elif index == "Accuracy":
      temp_dict['acc'] = float(value)
    elif index == "F-Measure":
      temp_dict['f'] = float(value)
    elif index == "Features are":
      temp_dict['features'] = value

"""
Sorting it in reverse order by the f_meaure so that I could see for what features / folds / is the f-meaure highest
"""

sorted_by_f = sorted(total_file, key = lambda x: x['f'], reverse = True)

#feature_list = list()
#for ii in range(0, 1000):
#  feature_list.append(sorted_by_f[ii]['features'])
#print list(set(feature_list))    

filter_by_feature = list()
for ii in sorted_by_f:
  if ii['features'].strip() == "bonus frac_to_poi shared_receipt_with_poi exercised_stock_options" and ii['fold'] == 2:
    filter_by_feature.append(ii)

filter_by_feature = sorted(filter_by_feature, key = lambda x:x['num'])
#print len(filter_by_feature)
#for ii in filter_by_feature:
#   #print ii['features']
#   print str(ii['f']) + " ", 
#   print ii['num']

plt.plot([ii['num'] for ii in filter_by_feature], [ii['f'] for ii in filter_by_feature], marker = "o", linestyle = "--", color = 'b')
plt.xlabel("Number of Estimators")
plt.ylabel("F-Measure")
plt.title("F-Measure vs Estimators with  B,FrPOI,ShrPOI,ESO at 2cc")
plt.savefig("F_Measure vs Estimators with B,FrPOI,ShrPOI,ESO at 2cc.png", transparent = True)
