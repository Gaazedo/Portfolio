def porcentagem_vet(vetor):
  count = 0 
  n = len(vetor)
  for i in range (n):
    if(vetor[i]==6):
      count +=1
    porcentagem = (count/50) *100
  return porcentagem

def ler_vetor(vetor):
  n = len(vetor)
  for i in range(n):
    vetor[i] = int(input("digite a qtd de numero de 1 a 6, que foi obtido através da rolagem do dado: "))

vetor = [0]*5
ler_vetor(vetor)
print("O percentual de ocorrencias da face 6 do dado dentre esses 50 lançamentos do dado é de{}%".format(porcentagem_vet(vetor)))