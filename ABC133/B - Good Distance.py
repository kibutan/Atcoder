import math
from decimal import Decimal

n,d = list(map(int,input().split()))
x = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dist = 0
for i in range(n-1):
  for j in range(i+1,n):
    for k in range(d):
#      print("i",i,"j",j,"k",k,"x[i][k]",x[i][k],"x[j][k]",x[j][k])
      dist += (x[i][k]-x[j][k])**2
#      print("dist +=",(x[i][k]-x[j][k])**2)
#    print("dist",dist,str(dist).isdigit())
    dist = Decimal(math.sqrt(dist))
    if(str(dist).isdigit()):
#      print("ans+")
      ans +=1
    dist = 0
print(ans)
