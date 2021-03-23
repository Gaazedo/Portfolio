def conta(vetor): 
  n=len(vetor)
  count=0
  for i in range (n):
    if vetor[i]>vetor[i-1] or vetor[i]<vetor[i-1]:
      count+=1
  return count



def lervetor(vetor):
  n=len(vetor)
  for i in range (n):
    vetor[i]=int(input("Digite um número: "))

