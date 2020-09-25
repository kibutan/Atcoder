N = int(input())
keta = 0
for i in range(10**9):
  if(N < 26 ** i):
    keta += i
    break
ans = [0]*keta
check = 0
if(N):
  for i in range(1,keta+1):
    j = (N-1)//(26**(keta-i))
    ans[check]=j
    check+=1
    N-=(j)*(26**(keta-i))
  for i in range(keta-1):
    print(chr(ans[i]+96),end="")
print(chr(ans[keta-1]+97))
