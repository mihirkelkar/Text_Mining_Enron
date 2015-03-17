#The three dimensions of the graph in this case happen to be the 3 most important function words that get selected after the singular value decomposition. 

import pandas as pd
import sys
import numpy as np
import pylab
import glob
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

def main():
  person_name = sys.argv[1]
  word_size = sys.argv[2]
  author_list = list()
  fp = open("../../author_length_list", "r")
  counter = 0
  while counter < 20:
    author_list.append(fp.readline().strip().split(":")[0].split("/")[-2])
    counter += 1
  print "Author list extracted"
  term_document_matrix = list()
  working_path = "/Users/mihirkelkar/code/Text_Mining_Enron/Authors_Emails_Block_Groups/" + person_name + "/trigrams/" + word_size + "/*"
  temp_files_list = glob.glob(working_path)
  for file in temp_files_list:
    fp = open(file, 'r')
    temp_doc = fp.readlines()
    temp_doc = [float(ii.split(":")[1]) for ii in temp_doc]
    term_document_matrix.append(temp_doc)
  tdm = [[term_document_matrix[j][i] for j in range(len(term_document_matrix))] for i in range(len(term_document_matrix[0]))]
  print "Doing SVD Now to reduce 3 dimensions"
  U, sigma, V = np.linalg.svd(tdm, full_matrices = False)
  v_df = pd.DataFrame(V, columns = temp_files_list)
  vector = np.matrix(V[:3, :])
  vector_x = list(np.array(vector[0]).reshape(-1,))
  vector_y = list(np.array(vector[1]).reshape(-1,))
  vector_z = list(np.array(vector[2]).reshape(-1,))
  #print vector_x
  #print "---------------"
  #print vector_y
  #print "---------------"
  #print vector_z
  #print "---------------"
  fig = pylab.figure()
  ax = Axes3D(fig)
  ax.scatter(vector_x, vector_y, vector_z)
  pyplot.savefig(person_name + "_Email_Block_Similarity_" + "_Word_Trigrams_Size_" + word_size)
main()
