def soma_imposto(custo,taxa_imposto):
    preco = custo +(custo * taxa_imposto/100) 
    return preco
 

x = float(input("Digite o valor de custo:"))
y = float(input("Digite o valor de porcentagem de imposto:"))
result = soma_imposto(x,y)

print("O preço final do produto é:",result)
 
