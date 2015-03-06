#Let us try and create a term document matrix here. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
  print "In here"
  no_terms_col  = sys.argv[1]
  term = sys.argv[2]
  number = sys.argv[1]
  author_list = list()
  fp = open("../author_length_list", "r")
  counter = 0
  while counter < 20:
    author_list.append(fp.readline().strip().split(":")[0].split("/")[-2])
    counter += 1
  print "Author list extracted"  
  term_document_matrix = list()
  if term == 'f':
    term = 'function_words'
    block_size = int(raw_input("What block size 1000 or 2000?"))
    for ii in author_list:
      print "making the term doc matrix"
      temp = open('../User_vectors/%s/vectors/function_words_%s_%s' %(ii, number, block_size))
      temp_doc = temp.readlines()
      temp_doc = [float(ii.split()[1]) for ii in temp_doc]
      term_document_matrix.append(temp_doc)
    

  elif term == 'b':
    for ii in author_list:
      temp = open('../User_vectors/%s/bigrams/bigrams_%s_5000' %(ii, number))
      temp_doc = temp.readlines()
      temp_doc = [float(ii.split(",")[1]) for ii in temp_doc]
      term_document_matrix.append(temp_doc)

  elif term == 't':
    for ii in author_list:
      term = 'trigrams'
      temp = open('../User_vectors/%s/trigrams/trigrams_%s_5000' %(ii, number))
      temp_doc = temp.readlines()
      temp_doc = [float(ii.split(",")[1]) for ii in temp_doc]
      term_document_matrix.append(temp_doc)
  print len(term_document_matrix), len(term_document_matrix[0])
  words = temp.readlines()[0:20]
  try:
    words = [ii.split(",")[0] for ii in words]
  except:
    words = [ii.split()[0] for ii in words]
  #Need to Transpose the matrix so that we have the term listed as rows and the columns listed as documents
  tdm = [[term_document_matrix[j][i] for j in range(len(term_document_matrix))] for i in range(len(term_document_matrix[0]))]
  
  print "Doing svd now"
  U, sigma, V = np.linalg.svd(tdm, full_matrices = False)
  v_df = pd.DataFrame(V, columns = author_list)
  v_df.apply(lambda x:np.round(x, decimals = 3))
  dist_df = pd.DataFrame(index=v_df.columns, columns = v_df.columns)
  for cname in v_df.columns:
    dist_df[cname] = v_df.apply(lambda x: dist(v_df[cname].values, x.values, sigma))
  print "Plotting Graph now"
  plt.imshow(dist_df.values, interpolation='none')
  ax = plt.gca()
  plt.xticks(xrange(len(dist_df.columns.values)))
  plt.yticks(xrange(len(dist_df.index.values)))
  ax.set_xticklabels(dist_df.columns.values, rotation = 90)
  ax.set_yticklabels(dist_df.index.values)
  plt.title("Author Similarity Grid")
  plt.colorbar()
  plt.savefig("200_Trigram_Similarity Matrix")

  
def dist(col1, col2, sigma):
  return np.linalg.norm(np.array(col1 - col2) * sigma) 

if __name__ == "__main__":
  main()  
