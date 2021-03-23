def ler_vetor():
  n = int(input("Qual o tamanho do Vetor? "))
  v = [0] * n
  for i in range (n):
    v[i] = int(input(f'valor da posição {i}: '))
  return v