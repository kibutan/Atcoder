# 参考
# https://qiita.com/gogotealove/items/11f9e83218926211083a
n,m = list(map(int,input().split()))
ks = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
cnt =0
ans = 0
on = []
k = []
s = []
for i in range(m):
  k.append(ks[i][0])
  s.append(ks[i][1:])
#print("ks",ks)
#print("k",k)
#print("s",s)
#for i in range(2**n):
#  flag = 1
#  bit = []
#  for j in range(n):
#    if((i >> j)&1):
#      bit.append(j+1)
#  print(bit)
for i in range(2**n):
  flag = 1
  bit = []
  for j in range(n):
    if((i >> j)&1):
      bit.append(j+1)
#  print("bit",bit)
  for x in range(m):
    cnt = 0
    for i in bit:
#      print("i",i)
#      print("s[",x,"]=",s[x],"have i = ",i," is",i in s[x])
      if(i in s[x]):cnt += 1
#    print("p[",x,"]=",p[x]," equal to cnt = ",cnt," % 2 is",cnt % 2 == p[x])
    if(cnt % 2 != p[x]):
#      print("Pass")
      break
    elif(cnt%2 == p[x] and x == (m-1)):ans+=1
print(ans)
    
  
