from itertools import accumulate

n = int(input())
a = list(map(int,input().split()))
acm = [0] + list(accumulate(a))
# print(list(acm))

for k in range(1,n+1):#数の長さk
  ans = 0
  for j in range(n+1-k):
    ans = max(ans,(acm[k+j]-acm[j]))
  print(ans)
