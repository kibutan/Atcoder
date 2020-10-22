N = list(map(int,input().split()))
flag = 0
res10000 = -1
res5000 = -1
res1000 = -1

for i in range(N[0]+1):
  for j in range(N[0]+1-i):
#    print(j*5000)
    if(N[1] == i * 10000 + j * 5000 + (N[0]-i-j) *1000):
      res10000 = i
      res5000 = j
      res1000 = (N[0]-i-j)
      break
print(res10000,res5000,res1000)
