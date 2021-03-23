from utility import*

def inverte(vet, vet2):
    n = len(vet)
    soma = 0
    for i in range (n):
        vet2[n-i-1] = vet[i]

