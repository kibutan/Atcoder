n,x = list(map(int,input().split()))
m = [int(input()) for i in range(n)]
ans = 0
for i in m:
  x -= i
  ans += 1

while x >= min(m):
  x -= min(m)
  ans += 1
print(ans)
