import collections
h,w = list(map(int,input().split()))
s = [input() for _ in range(h)]
cnt = 0
ans = 0
for i in range(0,h-1):
  for j in range(0,w-1):
    for n in range(2):
      for m in range(2):
#        print(s[i+n][j+m],end = "")
        if(s[i+n][j+m] == "#"):cnt += 1
#      print()
    if(cnt %2!= 0):ans+= 1
#    print(cnt)
    cnt = 0
print(ans)
#    print("s",s[i-1:i][j-1:j])
#    print("c",c)
#    if(c["#"] %2 != 0 ):cnt += 1
