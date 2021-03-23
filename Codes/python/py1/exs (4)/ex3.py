from utility import *

def cont(v, e):
  n= len(v)
  for i in range(n):
    if e == v[i]:
      return True
  return False

def intersec(a,b):
  r = ''

  n = len(a)
  for i in range (n):

    if cont(b,a[i]):
      r = r + str(a[i]) + ' '
  return r
