import os
import subprocess

def calculate_user_function_vectors():
  fp = open("../author_length_list", "r")
  author_list = fp.readlines()[0:20]
  for ii in author_list:
    user = ii.strip().split(":")[0].split("/")[-2]
    print user
    if not os.path.isdir(user + "/trigrams"):
      os.makedirs(user + "/" + "trigrams")
    for jj in ["50", "200"]:
      for kk in ["5000"]:
        subprocess.call(["python", "email_parser_trigram.py", user, jj, kk])
    print "Done creating trigrams for %s" %user
calculate_user_function_vectors()
