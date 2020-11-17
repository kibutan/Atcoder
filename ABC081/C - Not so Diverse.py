import collections
ans = 0
min_value = 0
N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
C = collections.Counter(A)
sorted_C = sorted(C.values())
#print(sorted_C)
if(len(C) > K):
  for i in range(len(C)-K):
    ans += sorted_C[i]
print(ans)
