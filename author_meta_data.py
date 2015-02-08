import email
import glob
import nltk
import string

from nltk.tokenize import sent_tokenize, word_tokenize

def clean_up(word_tokens):
  #Remove the tokens that contain http or contain the internal domain xgate.
  word_tokens = filter(lambda x: 'http' not in x and 'www' not in x , word_tokens)
  word_tokens = [x for x in word_tokens if x[-3:] != 'com' and x[-4:] != 'html']
  #clean out words that contain numerals in them.
  word_tokens = filter(lambda x: not any(ii.isdigit() for ii in x), word_tokens)
  return word_tokens

user_folders = glob.glob('/Users/mihirkelkar/code/Text_Mining_Enron/Length_data/*')
file = open('author_meta_data', 'a')
for user in user_folders:
  print user
  sent_emails_path = user + '/sent_items/*'
  print sent_emails_path
  sent_emails = glob.glob(sent_emails_path)
  print len(sent_emails)
  word_tokens_count = 0
  max_email_word_count = 0
  min_email_word_count = float("inf")
  for emails in sent_emails:
    print emails
    email_file = open(emails, 'r')
    current_email = email.message_from_file(email_file)
    cur_mail_content = current_email.get_payload().split("-----Original Message-----")[0]
    sent_tokens = sent_tokenize(cur_mail_content)
    temp_token_count = 0
    for sent in sent_tokens:
      sent = "".join([ii if ii not in string.punctuation else"" for ii in sent.lower()])
      temp_token_count += len(clean_up(word_tokenize(sent)))
    if temp_token_count > max_email_word_count:
      max_email_word_count = temp_token_count
    if temp_token_count < min_email_word_count:
      min_email_word_count = temp_token_count
    word_tokens_count += temp_token_count
  print word_tokens_count
  file.write("***********************")   
  file.write("Author_Name : %s\n" %user)
  if sent_emails:
    file.write("Average Email Word Length : %s words\n" %((word_tokens_count) / len(sent_emails)))
  file.write("Max Email Length : %s words\n" % max_email_word_count)
  file.write("Min Email Length : %s words\n" % min_email_word_count)   
