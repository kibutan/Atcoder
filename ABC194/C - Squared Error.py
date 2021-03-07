import numpy as np
n = int(input())
a = list(map(int, input().split()))
ans = 0
ans1 = 0
ans2 = 0
for i in range(n):
  ans1 = ans1 + a[i]**2
  ans2 = ans2 + a[i]
#  print(ans1)
#  print(ans2)  
print((ans1*n) - (ans2**2))
