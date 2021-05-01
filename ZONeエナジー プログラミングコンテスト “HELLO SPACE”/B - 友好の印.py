from decimal import Decimal
n,D,H= list(map(int,input().split()))
dh = [list(map(int,input().split())) for _ in range(n)]

def solve(d,h):
  if(Decimal(D*h -d*H)/(D-d) > 0):return Decimal(D*h -d*H)/(D-d)
  else:return 0

hight = 0
for i in range(n):
  hight = max(hight,solve(dh[i][0],dh[i][1]))
print(hight)
