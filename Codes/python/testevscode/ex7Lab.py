import math
def somaN(n):
    soma = 0
    for k in range (1,n+1):
        soma += (k/math.pow(k,2)) * (math.pow(-1,k +1))
    return soma

print(somaN(6))
