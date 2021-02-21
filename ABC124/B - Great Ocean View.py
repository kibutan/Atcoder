n  = int(input())
h = list(map(int,input().split()))
ans = 0
hight = 0
for i in range(len(h)):
#  print(hight)
  if(hight <= h[i]):
    ans+=1
    hight = h[i]
  else:continue
print(ans)
