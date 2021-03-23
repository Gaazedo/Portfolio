def PRIMO(num):
    div = 0
    i = 1
    while i <= num:
        if num % i ==0 :
            div = div + 1
            i = i + 1


    if div == 2:
        return True
    else:
        return False


num = int(input("Digite o 1° número inteiro: "))
num2 = int(input("Digite o 2° número inteiro: "))

for numero in range(num, num2 + 1,1):
    if PRIMO(numero):
        print("é primo",numero)

    else:
        print(" não é primo",numero)

