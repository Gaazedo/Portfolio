#MENSAGEM USER
def Msg():
  print("Este programa permite ao usuário converter temperaturas: ")
  
#VOID CONVERSAO
def Convert():
  while True:
    decisao = input("Escolha entre F ou C: ").capitalize()
    if decisao != "C" and decisao != "F":
      print("Por favor, escolha entre F ou C")
      continue
    else:
      print("Sua escolha foi {decisao}")
      break
  return decisao

#F°/C°
def exibeFahrenheitCelsius(start, end):
  C0 = (start - 32) * 5/9
  C1 = (end - 32) * 5/9

  print("A sua faixa de temperatura será,",C0,"até",C1)

  return 

def exibeCelsiusFahrenheit(start, end):
  C2 = (start * 9/5) + 32
  C3 = (end * 9/5) + 32

  print("A sua faixa de temperatura será,",C2,"até",C3)

  return 



Msg()

result = Convert()

T1 = float(input("Qual sua temperatura inicial? "))
T2 = float(input("Qual sua temperatura final? "))

if result == "F":
  exibeFahrenheitCelsius(T1,T2)
else:
  exibeCelsiusFahrenheit(T1,T2)
