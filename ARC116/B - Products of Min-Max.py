import itertools


n=int(input())
a=list(map(int,input().split()))

ans = 0
for i in range(2**n):
  bit_list=[]
#  print("pattern{}:".format(i),end="")
  for j in range(n):
    if((i >> j)&1):
      bit_list.append(a[j])
  if(bit_list == []):continue
  else:ans = ans + int((max(bit_list) * min(bit_list))) 
print(ans%998244353)  
