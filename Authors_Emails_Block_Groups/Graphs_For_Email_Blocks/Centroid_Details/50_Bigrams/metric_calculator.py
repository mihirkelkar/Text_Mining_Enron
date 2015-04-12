import glob
import os
import math

file_list = glob.glob('/Users/mihirkelkar/code/Text_Mining_Enron/Authors_Emails_Block_Groups/Graphs_For_Email_Blocks/Centroid_Details/50_Bigrams/*')

centroids_3d = {}
centroids_2d = {}
for ii in file_list:
  if "metric" in ii:
    continue
  fp = open(ii, 'r')
  temp = fp.readlines()
  centroids_3d[ii] = [float(jj) for jj in temp[0].strip().split(',')]
  centroids_2d[ii] = [float(jj) for jj in temp[2].strip().split(',')]

td_centroid_distances = {}
td = centroids_3d.items()
for ii in range(len(td)):
  rem_items  = td[:ii] + td[ii + 1:]
  c_to_c = 0
  for jj in rem_items:
    c_to_c += math.sqrt((td[ii][1][0] - jj[1][0])**2 + (td[ii][1][1] - jj[1][1]) ** 2 + (td[ii][1][2] - jj[1][2]) ** 2)
    td_centroid_distances[td[ii][0].split("/")[-1]] = float(c_to_c)/float(len(rem_items))

print td_centroid_distances

twod_centroid_distances = {}
td = centroids_2d.items()
for ii in range(len(td)):
  rem_items  = td[:ii] + td[ii + 1:]
  c_to_c = 0
  for jj in rem_items:
    c_to_c += math.sqrt((td[ii][1][0] - jj[1][0])**2 + (td[ii][1][1] - jj[1][1]) ** 2)
    twod_centroid_distances[td[ii][0].split("/")[-1]] = float(c_to_c)/float(len(rem_items))

#print twod_centroid_distances
