n,m = list(map(int,input().split()))
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
ans = 0

for i in range(n):
  if(s[i][3:] in t):
#    print("Plus" ,s[i][3:])
    ans += 1
    continue
    
print(ans)
