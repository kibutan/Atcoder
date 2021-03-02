n,T = list(map(int,input().split()))
ct = [map(int,input().split()) for _ in range(n)]
c,t = [list(i) for i in zip(*ct)]
ans = 10000
for i in range(n):
  if(t[i] <= T):
    ans = min(ans,c[i])
if(ans == 10000):ans = "TLE"
print(ans)
