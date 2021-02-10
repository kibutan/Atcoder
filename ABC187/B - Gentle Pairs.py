from decimal import Decimal
n  = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
x,y = [list(i) for i in zip(*xy)]
#print(x,y)
cnt = 0
for i in range(0,n-1):
  for j in range(i+1,n):
    if( -1 <= Decimal((y[i]-y[j])/(x[i]-x[j])) <= 1):cnt += 1
print(cnt)
