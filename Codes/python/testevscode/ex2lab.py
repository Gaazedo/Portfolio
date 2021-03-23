def sinal (a):
  if a > 0:
    return "P"
  else:
    return "N"


a = int(input("Insira o número para ver se ele é positivo ou negativo: "))

print(sinal(a))
