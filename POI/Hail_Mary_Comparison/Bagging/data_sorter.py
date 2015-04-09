"""
  writing a general library to convert given data from the doctionary format to a python grid. 
"""

import numpy as np


def featuresProcess(dict, features, remove=True, remove_all_zeroes=True, remove_any_zeroes = False, sort_stuff = False):
  
  """ 
        convert dictionary to numpy array of features
        remove = True will convert "NaN" string to 0.0
        remove_all_zeroes=True will remove any data points for which
        all the features you seek are 0.0
        remove_any_zeroes=True will omit any data points for which
            any of the features you seek are 0.0
  """
  retval = list()
  if sort_stuff:
    keys = sorted(dict.keys())
  else:
    keys = dict.keys()
  for ii in keys:
    temp_list = list()
    for jj in features:
      try:
        val = dict[ii][jj]
      except:
        print "error"
        return 
      if val == "NaN" and remove:
        val = 0
      temp_list.append(float(val))
    if remove_all_zeroes:
      all_z = True
      for item in temp_list:
        if item != 0 and item != 'NaN':
          flag = True

    if remove_any_zeroes:
      any_z = False
      if 0 in temp_list or "NaN" in temp_list:
        flag = False

    if flag:
      retval.append(np.array(temp_list))
  return np.array(retval)

def split(data):
  """
    Given a numpy array as in the function above. Seaprate the first feature and 
    put it on its own list. 
  """
  target = list()
  feature = list()
  for ii in data:
    target.append(ii[0])
    feature.append(ii[1:])
  return target, feature  



