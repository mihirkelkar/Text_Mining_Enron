import glob
import pandas as pd
import sys
import numpy as np
import pylab
import random

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

def main():
  person_one = sys.argv[1]
  person_two = sys.argv[2]
  word_size = sys.argv[3]
  term_document_matrix_one = list()
  term_document_matrix_two = list()
  working_path = "/Users/mihirkelkar/code/Text_Mining_Enron/Authors_Emails_Block_Groups/"
  path_one = working_path + person_one + "/vectors/" + word_size + "/*" 
  path_two = working_path + person_two + "/vectors/" + word_size + "/*"
  temp_file_list = glob.glob(path_one)
  for file in temp_file_list:
    fp = open(file, 'r')
    temp_doc = fp.readlines()
    temp_doc = [float(ii.split(":")[1]) for ii in temp_doc]
    term_document_matrix_one.append(temp_doc)
  tdm_one = [[term_document_matrix_one[j][i] for j in range(len(term_document_matrix_one))] for i in range(len(term_document_matrix_one[0]))]
  print "Doing SVD for the first one now."
  U, sigma, V = np.linalg.svd(tdm_one, full_matrices = False)
  v_df = pd.DataFrame(V, columns = temp_file_list)
  vector = np.matrix(V[:3, :])
  vector_x_one = list(np.array(vector[0]).reshape(-1,))
  vector_y_one = list(np.array(vector[1]).reshape(-1,))
  vector_z_one = list(np.array(vector[2]).reshape(-1,)) 
  temp_file_list = glob.glob(path_two)
  for file in temp_file_list:
    fp = open(file, 'r')
    temp_doc = fp.readlines()
    temp_doc = [float(ii.split(":")[1]) for ii in temp_doc]
    term_document_matrix_two.append(temp_doc)
  tdm_two = [[term_document_matrix_two[j][i] for j in range(len(term_document_matrix_two))] for i in range(len(term_document_matrix_two[0]))]
  print "Doing SVD for the second one now."
  U, sigma, V = np.linalg.svd(tdm_two, full_matrices = False)
  v_df = pd.DataFrame(V, columns = temp_file_list)
  vector = np.matrix(V[:3, :])
  vector_x_two = list(np.array(vector[0]).reshape(-1,))
  vector_y_two = list(np.array(vector[1]).reshape(-1,))
  vector_z_two = list(np.array(vector[2]).reshape(-1,))

  fig = pylab.figure()
  ax = Axes3D(fig)
  ax.scatter(vector_x_one, vector_y_one, vector_z_one, color = 'red')
  ax.scatter(vector_x_two, vector_y_two, vector_z_two, color = 'green')
  #pyplot.scatter(vector_x_one, vector_y_one, color = 'red')
  #pyplot.scatter(vector_x_two, vector_y_two, color = 'green')
  pyplot.savefig("Comparison_3d_noisy_temp" + "_Mann_vs_Krominski")

if __name__ == "__main__":
  main()

 




