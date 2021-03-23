def intersecao(vetA,vetB):
  vf=[]
  for i in vetA:
    if i in vetB:
      vf.append(i)
  return vf


def bubbleSort(c):
  for passnum in range(len(c)-1,0,-1):
    for i in range(passnum):
      if c[i] > c[i+1]:
        temp = c[i]
        c[i] = c[i+1]
        c[i+1] = temp 
  return c



vetA = [3, 6, 2, 8, 10, 1]
vetB =  [4, 2, 5, 1, 9]
c = intersecao(vetA,vetB)
print(bubbleSort(c))
