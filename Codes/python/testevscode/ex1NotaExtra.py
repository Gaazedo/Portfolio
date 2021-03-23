#DEFINIR 
Mcidades = [[0,63,210,190,0,190],[63,0,160,150,95,0],[210,160,0,10,0,0],[190,150,10,0,0,0],[0,95,0,0,0,80],[190,0,0,0,80,0]]
Mcaminho = [3,4,2,5,6,1]
totalizado = 0

#CORE
for i in range(1,(len(Mcaminho))):
    totalizado+=(Mcidades[Mcaminho[i-1]-1])[Mcaminho[i]-1]
    
#RESULTADO
print(totalizado)
