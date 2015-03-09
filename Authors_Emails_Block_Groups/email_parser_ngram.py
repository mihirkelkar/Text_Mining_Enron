import email
import glob
import itertools
import math
import nltk
import re
import string
import sys


from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from random import shuffle
from random import choice

def parse_directory():
  corpus_tokens = list()
  working_path = "/Users/mihirkelkar/code/Text_Mining_Enron/Length_data/" + sys.argv[1]
  corpus_tokens += parse_emails(working_path + "/")
  #for ii in range(0, 100):
  #  shuffle(corpus_tokens)
  new_corpus_tokens = list()
  blocksize = int(sys.argv[3])
  while True:
    temp_block = list()
    if len(corpus_tokens) > blocksize:
      for ii in range(blocksize):
        temp_block.append(corpus_tokens.pop(0))
    else:
       while corpus_tokens:
         temp_block.append(corpus_tokens.pop(0))
    temp_block = Counter(temp_block)
    new_corpus_tokens.append(temp_block)
    if not corpus_tokens:
      break
  return new_corpus_tokens

def parse_emails(working_path):
  """
  When within a user/sent_mail dir, then go ahead and call the parse_email_tokens on all files. 
  """
  total_user_tokens = list()
  ii = 'sent_items/*'
  temp_work_path = working_path + ii
  list_of_emails = glob.glob(temp_work_path) 
  for email in list_of_emails:
    total_user_tokens += parse_email_tokens(email)
  return total_user_tokens
    
def parse_email_tokens(cemail):
  "physically parses the file"
  file = open(cemail, 'r')
  current_email = email.message_from_file(file)
  curmail = current_email.get_payload().split("-----Original Message-----")[0]
  sent_tokens = sent_tokenize(curmail.lower())
  word_tokens = list()
  for sent in sent_tokens:
    sent = "".join([ii if ii not in string.punctuation else "" for ii in sent.lower()])
    word_tokens += nltk.ngrams(clean_up(word_tokenize(sent)), 3)
  return word_tokens


def clean_up(word_tokens):
  #Remove the tokens that contain http or contain the internal domain xgate. 
  word_tokens = filter(lambda x: 'http' not in x and 'www' not in x , word_tokens)
  word_tokens = [x for x in word_tokens if x[-3:] != 'com' and x[-4:] != 'html']
  #clean out words that contain numerals in them. 
  word_tokens = filter(lambda x: not any(ii.isdigit() for ii in x), word_tokens)
  return word_tokens  

def main():
  #Every time you run this script change this print. 
  print "Making vectors for " +  sys.argv[3] + " block length with " +  sys.argv[2] + " function words"
  slice = sys.argv[2]
  fp = open("../trigram_token_list", "r")
  function_words = list()
  counter = 0
  while counter < 200:
    temp_line = fp.readline().strip().split()
    x = temp_line[0]
    y = temp_line[1]
    z = temp_line[2]
    function_words.append((x, y, z))
    counter += 1
  temp = parse_directory()
  ctr = 1
  for block in temp:
    final_counter = {}
    for ii in function_words:
      try:
        somevar = final_counter[ii]
        final_counter[ii] = somevar + block[ii]  
      except:
        final_counter[ii] = block[ii] 

    kp = open(sys.argv[1] + "/trigrams/" + slice + "/" + "trigrams" + "_" +  str(ctr), "w")
    for word_vector in function_words[0:int(slice)]:
      kp.write(word_vector[0] + " " + word_vector[1] + " " + word_vector[2] +  " : " + str(final_counter[word_vector]) + "\n")
    ctr += 1
    kp.close()
  fp.close()
 
if __name__ == "__main__":
  main()
