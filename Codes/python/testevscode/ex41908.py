#calculo da area
def Area(n1,n2):
    area = (n1*n2)/2
    return area
#MSG SOBRE O CODIGO
def Msg():
    print("Esse programa calcula a area de um triangulo")
    
#CORE DO CODIGO
Msg()

n1 = float(input("Digite a altura do triangulo: "))
while(n1<=0):
    float(input("ERRO!Digite novamente a altura do triangulo: "))
    
n2 = int(input("Digite o tamanho da base do triangulo: "))
while(n2<=0):
    float(input("ERRO!Digite novamente a base do triangulo: "))



print("A area do triangulo é: ",Area(n1,n2))
