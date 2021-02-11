from decimal import Decimal
n = int(input())
btc = 380000
xu = [map(str,input().split()) for _ in range(n)]
x,u = [list(i) for i in zip(*xu)]
ans = 0
for i in range(n):
  if(u[i] == "JPY"):ans += int(x[i])
  else:ans += Decimal(x[i])*btc
print(str(ans))
