def exibeCelsiusTOFahrenheit(start):
  f1 = (((start/5)*9) + 32)
  return f1

def exibeFahrenheitTOCelsius(start):
  c1 = (((start - 32)*5)/9)
  return c1



c1 = float
f1 = float


print("1 = Conversor de Celsius para Farenheit\n2 = Conversor de Farenheit para Celcius")
func = (int(input("Insira uma opção. ")))
while func != 1 and func != 2:
  print("Entrada inválida.")
  print("1 = Conversor de Celsius para Farenheit\n2 = Conversor de Farenheit para Celcius")
  func = (int(input("Insira uma opção. ")))


if func == 2:
  f1 = float(input("Insira insira a temperatura em Farenheit. "))
  print("A temperatura transformada é", exibeFahrenheitTOCelsius(f1), "graus Celcius.")
else:
  c1 = float(input("Insira insira a temperatura em Celcius. "))
  print("A temperatura transformada é", exibeCelsiusTOFahrenheit(c1), "graus Farenheit.")