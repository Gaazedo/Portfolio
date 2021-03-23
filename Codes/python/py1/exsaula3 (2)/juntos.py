import random

def exs():
  x=True
  while x:
    print("(1) Adicionar um novo elemento na próxima posição livre do vetor\n(2) Mostrar os elementos do vetor\n(3) Buscar um elemento no vetor\n(4) Inserir elemento de forma ordenada\n(5) Remover elemento\n(0) Sair do programa")
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
    elif escolha==3:
      print(busca_seq())
    elif escolha==4:
      print(inserir_ord())
    elif escolha==5:
      print(remover())

    else:
      x=False
      print("Fim")
  return vetor


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

def inserir_ord(v, qtd):
  ordenado = True
  for i in range(qtd):
    if v[i] > v[i - 1]:
      ordenado = True
    else:
      ordenado = False

    return ordenado




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
       





exs()