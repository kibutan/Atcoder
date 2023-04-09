n,d = list(map(int,input().split()))
t = list(map(int,input().split()))
for i in range(1,n):
#  print(i,i-1,t[i],t[i-1])
  if((t[i]-t[i-1]) <= d):
    print(t[i])
    exit()
else:print(-1)
