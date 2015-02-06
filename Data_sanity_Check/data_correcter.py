"""
Some email replies in folder like arnold-j/ dont have the ____original message____ tag. this messes with my scripts creating unecessary tokens that take up memory. Trying to correct this by actually adding the tag to all such emails. A first mock up for that script.This GODDAMM SCRIPT CURRENTLY WORKS 
"""

import glob
import re
import sys

test_folders = glob.glob('/Users/mihirkelkar/Desktop/thesis/enron/maildir/baughman-d/*')
test_folders = filter(lambda x: 'sent_items' in x, test_folders)
test_mails = list()
for folder in test_folders:
  test_mails += glob.glob(folder + '/*')
counter = 0
for test_mail in test_mails:
  read_this = open(test_mail, 'r')
  old_file = read_this.read()
  file = re.sub(r'--------- Inline attachment', '\n-----Original Message-----', old_file)
  file = re.sub(r'\n.+@ENRON', "\n-----Original Message-----", file)
  file = re.sub(r'-+\s*Forwarded\s*', "\n-----Original Message-----", file)
  file = re.sub(r'\n*".+"\s*<.+>',"\n-----Original Message-----", file)
  file = re.sub(r'\n*From:.+M', "\n-----Original Message-----", file)
  file = re.sub(r'<.+>.+M', "\n-----Original Message-----", file)
  file = re.sub(r'\.com.+M',"\n-----Original Message-----", file)
  if file != old_file:
    print test_mail
    counter += 1
  read_this.close()
  read_this = open(test_mail, 'w')
  read_this.write(file)
  read_this.close()
print counter
