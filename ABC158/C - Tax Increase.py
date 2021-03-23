a,b = list(map(int,input().split()))
ans = float("inf")
for i in range(1009):
  if(int(i * 8/100) == a and int(i * 10/100) == b):ans = min(ans, i)
if(ans != float("inf")):print(ans)
else:print(-1)
