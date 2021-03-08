import numpy as np
def mex(A , m):
  return min(A)
ans = float('inf')
n,m = list(map(int,input().split()))
a =list(map(int,input().split()))
ans_list = np.arange(n)
print(ans_list)
for i in range(n-m):
#  print(a[i:i+m])
  ans = min(ans,min(set(ans_list)^set(a[i:i+m])))
print(ans)
