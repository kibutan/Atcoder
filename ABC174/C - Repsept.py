import math
K = int(input())
ans = -1
a=[0]*1000001 #おそらく考えうるKの最大値のときのiの値
a[1] = 7%K
for i in range(2,K+1):
  a[i]=(a[i-1]*10+7)%K

for i in range(1,K+1):
  if((a[i]) == 0):
    ans = i
    break
print(ans)
