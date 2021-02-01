a,b,k = list(map(int,input().split()))
cd = []
for i in range(min(a,b),0,-1):
  if(a%i == 0 and b%i == 0):cd.append(i)
print(cd[k-1])
#print(cd)
