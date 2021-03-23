#feito com a ajuda da monitoria 

import random
def inserir_ord(v, qtd, e):
    if qtd == 0:
        v[0] = e
        return v
    else:
        for i in range(qtd): 
                x = i 
                break  
        else:
                v[i+1] = e 
                return v
        v = v[:x] + [e] + v[x:] 
        return v



def intercalar_ord(v1, v2, vf):
    aux1 = 0
    aux2 = 0
    for i in range(len(vf)):
        if aux1 == len(v1):
            vf[i] = v2[aux2]
            aux2 += 1
        elif aux2 == len(v2):
            vf[i] = v1[aux1]
            aux1 += 1            
        elif v1[aux1] <= v2[aux2]:
            vf[i] = v1[aux1]
            aux1 += 1
        else:
            vf[i] = v2[aux2]
            aux2 += 1
    return vf
def contem(v, qtd, e):
    for i in range(qtd):
        if v[i] == e:
            return True
    return False
def gerar(v1, v2):
    qtd_v1 = 0
    qtd_v2 = 0
    n = (len(v1) + len(v2)) * 5
    while (qtd_v1 < len(v1)):
        e = random.randint(1, n)
        print(f"e: {e}")
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v1 = inserir_ord(v1, qtd_v1, e)
            qtd_v1 += 1
        print(f"V1: {v1}")
    while (qtd_v2 < len(v2)):
        e = random.randint(1, n)
        print(f"e: {e}")
        if not contem(v1, qtd_v1, e) and not contem(v2, qtd_v2, e):
            v2 = inserir_ord(v2, qtd_v2, e)
            qtd_v2 += 1
        print(f"V2: {v2}")
n = int(input('Número de elementos em v1 e em v2: '))
v1 = [0] * n
v2 = [0] * n
vf = [0] * (len(v1) + len(v2))
gerar(v1, v2)
print('\nv1:', v1)
print('v2:', v2)
intercalar_ord(v1,v2,vf)
print('vf:', vf)