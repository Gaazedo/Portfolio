def intersecao(vetA, vetB):
  intern = []
  for x in range(0,11):
     if x in vetA and x in vetB:
       intern=x
  return intern

vetA = [3, 6, 2, 8, 10, 1]
vetB =  [4, 2, 5, 1, 9]


y=intersecao(vetA, vetB)
print(y)

 iguais = iguais+str(vetA[i])+","
 def ordenacao(vetC):
  n=len(vetC)
  for i in range(n):
    minimo = i
    for j in range(i+1,n):