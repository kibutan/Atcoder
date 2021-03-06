n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a,b = [list(i) for i in zip(*ab)]
ans = float('inf')

for i in range(n):
  for j in range(n):
    if(i == j):ans = min(ans,a[i]+b[j])
    else:ans = min(ans, max(a[i],b[j]))
print(ans)
