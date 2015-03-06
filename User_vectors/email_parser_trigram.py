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
  for ii in range(0, 100):
    shuffle(corpus_tokens)
  new_corpus_tokens = list()
  blocksize = int(sys.argv[3])
  for ii in range(0, blocksize):
    new_corpus_tokens.append(choice(corpus_tokens))
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
  trigram_tokens = list()
  for sent in sent_tokens:
    sent = "".join([ii if ii not in string.punctuation else "" for ii in sent.lower()])
    trigram_tokens += nltk.ngrams(clean_up(word_tokenize(sent)),3)
  return trigram_tokens


def clean_up(word_tokens):
  #Remove the tokens that contain http or contain the internal domain xgate. 
  word_tokens = filter(lambda x: 'http' not in x and 'www' not in x , word_tokens)
  word_tokens = [x for x in word_tokens if x[-3:] != 'com' and x[-4:] != 'html']
  #clean out words that contain numerals in them. 
  word_tokens = filter(lambda x: not any(ii.isdigit() for ii in x), word_tokens)
  return word_tokens  

def main():
  #Every time you run this script change this print. 
  print "Making trigrams for " +  sys.argv[3] + " block length with " +  sys.argv[2] + " function words"
  #Go change the counter for random.choice in the parse_directory function
  final_counter = {}
  slice = sys.argv[2]
  kp  = open(sys.argv[1] + "/trigrams/" + "trigrams_" + slice + "_" + sys.argv[3], 'w')
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
  for ii in range(50):
    temp = Counter(parse_directory())
    for ii in function_words:
      try:
        somevar = final_counter[ii]
        final_counter[ii] = somevar + temp[ii]
      except:
        final_counter[ii] = temp[ii]
  for ii in function_words[0:int(slice)]:
    kp.write(ii[0] + " " + ii[1]  + " " + ii[2] + ","+ str(math.floor(final_counter[ii] / 50)) + "\n")
  fp.close()
  kp.close()
 
if __name__ == "__main__":
  main()
