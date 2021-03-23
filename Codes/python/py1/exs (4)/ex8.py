def physics (vet1, vet2):
  frx = vet1[0]+ vet2[0]
  fry = vet1[1]+ vet2[1]
  frz = vet1[2]+ vet2[2]

  fr = [frx,fry,frz]
  return fr

print(physics([1,2,3],[1,2,3]))