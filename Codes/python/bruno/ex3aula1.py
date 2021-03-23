def soma_imposto(custo,taxa_imposto):
  return custo*((100+taxa_imposto)/100)

x = int(input("Insira o custo. "))
y = int(input("Insira a taxa de imposto. "))

print("Este é o valor do produto com imposto", soma_imposto(x,y))