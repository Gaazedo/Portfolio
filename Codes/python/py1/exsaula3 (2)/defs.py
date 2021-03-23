def ex1e2():
  x=True
  while x:
    print("(1) Adicionar um novo elemento na próxima posição livre do vetor\n(2) Mostrar os elementos do vetor\n(0) Sair do programa")
    escolha=int(input("Escolha uma opção: "))
    if escolha==1:
      v=int(input("Qual é o tamanho do vetor?"))
      vetor=[0]*v
      for j in range (len(vetor)):
        numero=int(input("Adicione um número: "))
        vetor[j]+=numero
        if (len(vetor)-(j+1))==0:
          print("Não há mais espaços no vetor")
        elif (len(vetor)-(j+1))==1:
          print("Resta apenas um espaço no vetor")
        else:
          print("Ainda há",(len(vetor)-(j+1)))
    elif escolha==2:
        print("O vetor criado é",vetor)

    else:
      x=False
      print("Fim")
  return vetor

ex1e2()

def busca_seq():
  qtd=int(input("Qual é o tamanho do vetor?"))
  vetor=[0]*qtd
  for j in range (qtd):
    numero=int(input("Adicione um número: "))
    vetor[j]+=numero
  
    print(vetor)
  elemento=int(input("Procure o elemento: "))
  count=1
  for i in range (len(vetor)):
    if vetor[i]!=elemento:
      count+=1
    elif vetor[i]==elemento:
      return count
  if elemento not in vetor:
    return -1

busca_seq()

def remover():
  qtd=int(input("Qual é o tamanho do vetor?"))
  vetor=[0]*qtd
  for j in range (qtd):
    numero=int(input("Adicione um número: "))
    vetor[j]+=numero
  elemento=int(input("Digite o elemento a ser removido: "))
  for i in range(len(vetor)-1):
    if elemento==vetor[i]:
      vetor[i:i+1]=[]
      return vetor
remover()

def inserir(v, qtd):
  ordena = True
  for i in range(qtd):
    if v[i] > v[i - 1]:
      ordena = True
    else:
      ordena = False

  return ordena

inserir()

