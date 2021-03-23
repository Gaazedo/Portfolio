def valor_pagamento(valor_prestacao, dias_atraso):
  if dias_atraso == 0:
    return valor_prestacao
  else:
    return ((valor_prestacao*1.03)+(valor_prestacao*(0.001*dias_atraso)))
op = 1
qnt = 0
pagamentos = []
soma = 0
print("1 = Calcular novo pagamento\n2 = Sair do programa")
p = int(input("Escolha uma opção. "))
while p != 1 and p != 2:
  print("Insira uma opção válida.")
  print("1 = Calcular novo pagamento\n2 = Sair do programa")
  p = int(input("Escolha uma opção. "))

while op != 2:
  if p == 1:
    x = int(input("Insira o valor da prestação. "))
    y = int(input("Insira os dias atrasados. "))
    print(valor_pagamento(x,y))
    qnt+=1
    pagamentos.append(valor_pagamento(x,y))
  else:
    for i in range(len(pagamentos)):
      soma += pagamentos[i]
    print("Foram calculados", qnt, "pagamento(s).")
    print("Todos eles somam", soma, "reais.")
  print("1 = Calcular novo pagamento\n2 = Sair do programa")
  p = int(input("Escolha uma opção. "))
  while p != 1 and p != 2:
    print("Insira uma opção válida.")
    print("1 = Calcular novo pagamento\n2 = Sair do programa")
    p = int(input("Escolha uma opção. "))