def inverter(vetor, ):
  menor=vetor[0]
  if len(vetor)==1:
    return menor
  else:
    return inverter(vetor[1::])+ menor

   





palavra = input("Palavra a ser invertida: ")
vetor = list(palavra)
resposta = ''.join(vetor)
print("A palavra invertida é:", inverter(vetor))