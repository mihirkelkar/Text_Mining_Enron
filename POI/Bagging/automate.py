import subprocess

learning_rate = [0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.6, 0.75, 0.9, 1.0, 1.1, 1.25, 1.5, 2.0, 2.5, 3.0]
estimators = [5,10,25,50,100,150,200,250,350,500,750,1000,2000,5000]
for ii in learning_rate:
  for jj in estimators:
    subprocess.call(["python", "starter_kit.py", str(jj), str(ii)])
    subprocess.call(["python", "ada.py", str(jj), str(ii)]) 

print "Done Lets Analyze How we learned things"   
