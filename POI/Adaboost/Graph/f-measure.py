fp = open('Ada_Boost_Optimal_performace', 'r')
data = fp.readlines()
kp = open("F_measure_Ada_optimal", "w")
for ii in data:
  temp = ii.strip().split(',')
  precision = float(temp[2].split(":")[1])
  recall = float(temp[3].split(" ")[2])
  if precision == 0 and recall == 0:
    continue
  else:
    f_measure = 2 * (precision * recall)
    f_measure /= (precision + recall)
    string_temp = "f_measure : " + str(f_measure)
    temp.append(string_temp)
    kp.write(",".join(temp))
    kp.write("\n")
kp.close()      
