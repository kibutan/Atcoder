#https://qiita.com/derodero24/items/91b6468e66923a87f39f
from operator import mul
from functools import reduce

def cmb(n,r):
  r = min(n-r,r)
  if r == 0: return 1
  over = reduce(mul,range(n, n-r , -1))
  under = reduce(mul, range(1,r+1))
  return over //under

ans = 0

L = int(input())
for i in range(0,11):
  ans = cmb(L-1,i+1)
  
print(ans)
