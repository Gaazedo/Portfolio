def achar(vetor1):
  m = len(vetor1)
  count=0
  for i in range(m):
    if vetor1[i]!='x':
      count+=1
    else:
      vetor1[i]=='x'
      return count
    return count
  

def ler_vetorx(vetor):
    m = len(vetor)
    for i in range(m):
        vetor[i] = input("Digite um número ou x (apenas uma vez): ")


 