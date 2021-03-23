from utility import*

def iguais(vetor1, vetor2):
    m1 = len(vetor)
    iguais = ''
    for i in range(m1):
        if (vetor1[i] not in vetor2):
            iguais = iguais + str(vetor[i]) + " "
    return iguais

