n,x = list(map(int,input().split()))
l = list(map(int,input().split()))
now = 0
ans = 1
for i in l:
  if(now + i <=x):
    ans+=1
    now += i
  else:break
print(ans)
