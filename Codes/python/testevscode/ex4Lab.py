def exibeCelsiusTOFahrenheit(start):
  f = (((start/5)*9) + 32)
  return f

def exibeFahrenheitTOCelsius(start):
  c = (((start - 32)*5)/9)
  return c



c = float
f = float


print("1 = Conversor de Celsius para Farenheit\n2 = Conversor de Farenheit para Celcius")
fun = (int(input("Insira uma opção: ")))
while fun != 1 and fun != 2:
  print("Entrada inválida.")
  print("1 = Conversor de Celsius para Farenheit\n2 = Conversor de Farenheit para Celcius")
  func = (int(input("Insira uma opção: ")))


if fun == 2:
  f = float(input("Insira insira a temperatura em Farenheit: "))
  print("A temperatura transformada é", exibeFahrenheitTOCelsius(f), "graus Celcius.")
else:
  c = float(input("Insira insira a temperatura em Celcius: "))
  print("A temperatura transformada é", exibeCelsiusTOFahrenheit(c), "graus Farenheit.")
