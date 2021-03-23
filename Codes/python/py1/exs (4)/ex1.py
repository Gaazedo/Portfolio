from utility import* 

def CresDecr(x):
  for i in range(len(x)):
    if x[i] > x[i-1]:
      return 'false'
    else:
      return 'true'

