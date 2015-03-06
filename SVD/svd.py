#Let us try and create a term document matrix here. 

import sys

def main():
  no_terms_col  = sys.argv[1]
  term = sys.argv[2]
  number = sys.argv[1]
  author_list = list()
  fp = open("../author_length_list", "r")
  counter = 0
  while counter < 20:
    author_list.append(fp.readline().strip().split(":")[0].split("/")[-2])
    counter += 1
  term_document_matrix = list()
  if term == 'f':
    term = 'function_words'
    block_size = int(raw_input("What block size 1000 or 2000?"))
    for ii in author_list:
      temp = open('../User_vectors/%s/vectors/function_words_%s_%s' %(ii, number, block_size))
      temp_doc = temp.readlines()
      temp_doc = [float(ii.split()[1]) for ii in temp_doc]
      term_document_matrix.append(temp_doc)
    

  elif term == 'b':
    for ii in author_list:
      temp = open('../user_vectors/%s/bigrams/bigrams_%s_5000' %(ii, number))
      temp_doc = temp.readlines()
      temp_doc = [float(ii.split(",")[1]) for ii in temp_doc]
      term_document_matrix.append(temp_doc)

  elif term == 't':
    term = 'trigrams'

  print len(term_document_matrix)
  print len(term_document_matrix[0])
if __name__ == "__main__":
  main()

    
