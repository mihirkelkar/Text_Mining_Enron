import os
import subprocess

def email_block_function_word_plot():
  fp = open("../../author_length_list", "r")
  #author_list = fp.readlines()[0:20]
  author_list = ["mann-k", "kaminski-v"]
  for ii in author_list:
    user = ii#.strip().split(":")[0].split("/")[-2]
    print user
    for jj in ["50"]:
      subprocess.call(["python", "email_graph_generator.py", user, jj])
    print "Graph made"

email_block_function_word_plot()
