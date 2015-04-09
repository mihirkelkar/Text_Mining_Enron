import matplotlib.pyplot as plt

plot_data = {}
fp = open('F_measure_Ada_optimal', 'r')
data = fp.readlines()
for ii in data:
  accuracy = float(ii.split(',')[-2].split(":")[1])
  iterators = float(ii.split(',')[1].split(":")[1])
  try:
    plot_data[iterators].append(accuracy)
  except:
    plot_data[iterators] = [accuracy]

temp_list = plot_data.items()
for ii in temp_list:
  ii[1].append(max(ii[1]))

sorted_list = sorted(temp_list, key = lambda x:x[0])
x = [ii[0] for ii in sorted_list]
y = [ii[1][-1] for ii in sorted_list]

print x
#print "- - - - -"
print y

plt.plot(x, y, marker='o', linestyle='--', color='r')
plt.xlabel('No of Estimators')
plt.ylabel('Accuracy')
plt.title('Accuracy vs number of Estimators')
plt.savefig('Accuracy_vs_Estimators.png', transparent = True)



















