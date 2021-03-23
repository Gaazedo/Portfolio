def contador(n,k):
  if n<k:
    return 0
  else:
    return 1 + contador (n-k,k)
   



n=int(input("Digite o número: "))
k=int(input("Digite o número: "))
print(contador(n,k))
