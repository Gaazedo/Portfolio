def sinal (a):
  if a > 0:
    return "P"
  else:
    return "N"


a = int(input("Insira o número e direi se ele é positivo (P), ou negativo(N). "))

print(sinal(a))