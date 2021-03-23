

#MENSAGEM USER
def Msg():
  print("Este programa permite ao usuário converter temperaturas: ")
  
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