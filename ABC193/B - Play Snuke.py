n = int(input())
apx = [list(map(int,input().split())) for i in range(n)]
a=[]
p=[]
x=[]
ans = float("inf")
for i in range(n):
  a.append(apx[i][0])
  p.append(apx[i][1])
  x.append(apx[i][2])

for i in range(n):
  if(a[i] < x[i]):
    ans = min(ans, p[i])
if(ans == float("inf")):print("-1")
else:print(ans)
