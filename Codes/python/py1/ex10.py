from ex3 import cont, intersec
from ex4 import iguais
from ex5 import iguais1
from ex6 import conta, lervetor
from ex7 import achar, ler_vetorx
from utility import ler_vetor


def menuprinc():
    opcao = int(
        input('''
Escolha um programa:
1 - ex3
2 - ex4
3 - ex5
4 - ex6
5 - ex7
0 - exit

Escolha:  '''))
    if opcao == 1:
      print('Conjunto A:')
      A = ler_vetor()

      print('Conjunto B:')
      B = ler_vetor()

      print('Intersecção:',intersec(A,B))
    elif opcao == 2:
      vetor = ler_vetor()
      vetor2 = ler_vetor()

      print("Os elementos apenas do vetor um são: ", iguais(vetor, vetor2))
    elif opcao == 3:
      vetor = ler_vetor()
      vetor2 = ler_vetor()

      print("A união dos dois vetores é  ", iguais(vetor, vetor2))
      
    elif opcao == 4:
      vetor=[0]*5
      lervetor(vetor)
      print("A quantidade de valores diferentes que existem no vetor é de: ",conta(vetor))
       
    elif opcao == 5:
      v = [0] * 5
      ler_vetorx(v)
      print("O X está na posição", achar(v))  
    elif opcao == 0:
      
      return print("fim")
    else:
      print("\nEste número não está nas alternativas, tente novamente :D.\n")


menuprinc()
