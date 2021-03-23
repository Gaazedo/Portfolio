def Maior(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
def Msg():
    print("Esse programa calcula o maior numero entre dois digitados")
    
#CORE
Msg()

n1 = int(input("Digite o Primeiro valor para comparar: "))
n2 = int(input("Digite o Segundo valor para comparar: "))

result = Maior(n1,n2)

print("O Maior entre os numeros digitados é: ",result)
