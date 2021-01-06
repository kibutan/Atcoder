import numpy as np
n,l = list(map(int,input().split()))
before_list = np.array([])
for i in range(n):
  before_list = np.append(before_list,l+(i+1)-1)
#print(before_list)
#print(int(sum(before_list)))
apple_ate = before_list[np.argmin(np.abs(before_list))]
print(int(sum(before_list)-apple_ate))
