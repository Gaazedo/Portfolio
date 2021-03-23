

import math
var = [6.57,6.77,5.60,6.05,6.31,7.98,6.96]
var2 = [45,25,35,50,25,15,40]
total = 0
dpvar = 0
dpvar2 = 0
for m in range(len(var)):
  dpvar += (var[m] - 66.60)**2
for n in range(len(var2)):
  dpvar2 += (var2[n] - 33.57)**2
dpvar2 = math.sqrt(dpvar2/6)
dpvar = math.sqrt(dpvar/6)
print("Desvio padrão dos números recebidos no R: " + str(dpvar))
print("Desvio padrão dos números recebidos no ex 4 (estrelas): " + str(dpvar2))


for i in range(len(var)):
  print("(" +  str(var[i]) + " -  66.60)(" + str(var2[i]) + " -  33.57)")
  total += (var[i] - 66.60)*(var2[i] - 33.57)

print("Total da somatória: " + str(total))
print("Total do cálculo: " + str(total/(6*dpvar*dpvar2)))