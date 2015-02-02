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
  for dir in [glob.glob(working_path)[1]]:
    corpus_tokens += parse_emails(dir + "/")
  return corpus_tokens

def parse_emails(working_path):
  """
  When within a user/sent_mail dir, then go ahead and call the parse_email_tokens on all files. 
  """
  print working_path
  print "Entered Parse Email function"
  working_path += "sent_items/*"
  print working_path
  list_of_emails = glob.glob(working_path) 
  total_user_tokens = Counter()
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
    word_tokens += word_tokenize(sent)  
  return Counter(word_tokens)
    
def main():
  print parse_directory()
  
if __name__ == "__main__":
  main()
