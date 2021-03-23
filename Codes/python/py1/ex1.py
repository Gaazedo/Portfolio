def q(n):
  if n==1:
    return n
  else:
    return q(n-1)+(2*n-1)



n=int(input("Digite um número: "))
print(q(n))
