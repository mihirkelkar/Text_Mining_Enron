import glob
import os

from commands import *

user_folders = glob.glob('/Users/mihirkelkar/code/Text_Mining_Enron/Length_data/*')
for user in user_folders:
  print user
  user_sub_dirs = glob.glob(user + '/*')
  print len(user_sub_dirs)
  if user + '/sent_items' not in user_sub_dirs:
    os.chdir(user)
    if user + '/sent' in user_sub_dirs: 
      command = "mv sent sent_items" 
      print getoutput(command)
    elif user + '/_sent_mail' in user_sub_dirs:
      command = "mv _sent_mail sent_items"
      print getoutput(command)


