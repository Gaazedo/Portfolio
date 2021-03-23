def Comb(n,k):
  if k==1:
    return n 
  if n==k:
    return 1
  if 1<k<n:
    return Comb (n-1,k-1) + Comb (n-1, k)


n=int(input("Digite o número de elementos: "))
k=int(input("Digite o número de grupos que se deseja agrupar: "))
print(Comb(n,k))
