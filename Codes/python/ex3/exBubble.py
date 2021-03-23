def intersecao(vetA, vetB):
    inter = [x for x in range(0,11) if x in vetA and x in vetB]
    return inter

a = [3, 6, 2, 8, 10, 1]
b = [4, 2, 5, 1, 9]
c = intersecao(a,b)
print(c)

def bubbleSort(c):
  for passnum in range(len(c)-1,0,-1):
    for i in range(passnum):
      if c[i] > c[i+1]:
        temp = c[i]
        c[i] = c[i+1]
        c[i+1] = temp 
  return c

