#spthx 
#https://engineeeer.com/python-multiple-lists/
import itertools
n,m = list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(m)]
ans = 0
cnt = 0
k = int(input())
cd = [list(map(int,input().split())) for _ in range(k)]
iter = list(itertools.product(*cd))
#print(list(itertools.product(*cd)))
for j in iter:
  cnt = 0
  for i in ab:
#    print("ab",*i)
#    print("iter",*j)
    if(i[0] in j and i[1] in j):
#      print("Yeeee")
      cnt+=1
    ans = max(ans,cnt)
#print("final",ans)
print(ans)
