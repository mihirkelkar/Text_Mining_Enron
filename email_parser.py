import email
import glob
import itertools
import nltk
import re
import string

from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

def parse_directory():
  corpus_tokens = Counter()
  print "Entered Parse Directory"
  working_path = "/Users/mihirkelkar/Desktop/thesis/enron/maildir/*"
  for dir in [glob.glob(working_path)[2]]:
    corpus_tokens += parse_emails(dir + "/")
  return corpus_tokens

def parse_emails(working_path):
  """
  When within a user/sent_mail dir, then go ahead and call the parse_email_tokens on all files. 
  """
  print working_path
  total_user_tokens = Counter()
  for ii in ['sent_items/*']:
    temp_work_path = working_path + ii
    print temp_work_path
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
    # *******************************************************
    print cemail
    print "--------------------------------"
    print clean_up(word_tokenize(sent))
    print '================================='
    print "*******************************************************"
    word_tokens += word_tokenize(sent)
    word_tokens = clean_up(word_tokens)
    #******************   TEMPORARY CODE HACK ****************
  #word_tokens = [(x, cemail) for x in word_tokens]
  return Counter(word_tokens)

def clean_up(word_tokens):
  #Remove the tokens that contain http or contain the internal domain xgate. 
  word_tokens = filter(lambda x: 'http' not in x and 'www' not in x , word_tokens)
  word_tokens = [x for x in word_tokens if x[-3:] != 'com' and x[-4:] != 'html']
  #clean out words that contain numerals in them. 
  word_tokens = filter(lambda x: not any(ii.isdigit() for ii in x), word_tokens)
  return word_tokens  
def main():
  print parse_directory()
  
if __name__ == "__main__":
  main()
