import random

def Mat(matriz,n_linhas, n_colunas):
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(random.randint(1,100))
        matriz.append(linha)

def Imprimir(matriz,n_linhas, n_colunas):
    for i in range(n_linhas):
        for j in range(n_colunas):
            print(matriz[i][j],end=" ")

        print("\n")

    return(' ')

def Ocorre(matriz1,matriz2):
    linhas1 = 20
    linhas2 = 20
    colunas1 = 20
    colunas2 = 20
    num_matriz1 = []
    num_matriz2 = []
    for i in range(linhas1):
        for j in range(colunas1):
            num_matriz1.append((matriz1[i][j]))
            num_matriz2.append((matriz2[i][j]))
    final = []
    for k in range(len(num_matriz1)):
        for j in range(len(num_matriz2)): 
            if num_matriz1[k]==num_matriz2[j]:
                if num_matriz1[k] not in final:
                    final.append(num_matriz1[k])

    print("Os valores da matriz 1 que aparecem na matriz 2 são:",final)

matriz1 = []
matriz2 = []

print("A matriz 1 é:")
Mat(matriz1,20,20)
Imprimir(matriz1,20,20)
print("A matriz 2 é:")
Mat(matriz2,20,20)
Imprimir(matriz2,20,20)
Ocorre(matriz1,matriz2)

