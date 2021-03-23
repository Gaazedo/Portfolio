salario = float(input("Digite seu salário: "))
pAumento = float(input("Digite o percentual de aumento do seu sálario: "))


AumentoSalario = (salario / 100) * pAumento
Nsalario = AumentoSalario + salario
print("o valor de aumento foi de: R$",AumentoSalario)
print("e seu novo salario será de: R$",Nsalario)