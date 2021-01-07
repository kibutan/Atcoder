# 参考
# https://qiita.com/gogotealove/items/11f9e83218926211083a
n,m = list(map(int,input().split()))
ks = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
cnt = 0
on = 0
for i in range(2**n):
  list = []
  
  for j in range(n):
    print("j",j)
    if((i >> j)&1):
      list.append(j+1) #Switch onの組み合わせをつくる[Swich1 on,Switch2 on]
      k = ks[j][0]
      s = ks[j][1:]
      print("s",s)
    for _ in list:
      print("_",_)
      print("_ in s = ",_ in s)
      if(_ in s):
        on += 1
        print("switch",_,"is on")
        print("power",j+1,"is",(on % 2 == p[j]))
    if(on % 2 == p[j]):
      print("True")
      continue
    else: 
      print("False")
      break
  print(list)
  cnt += 1
print(cnt)
