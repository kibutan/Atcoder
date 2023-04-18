import numpy as np
h,w = list(map(int,input().split()))
a=np.array([list(map(int,input().split())) for _ in range(h)]).T

for i in a:
  print(*i)
