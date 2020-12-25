from decimal import Decimal
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
  ans += Decimal(Decimal(1)/Decimal(a[i]))
print(Decimal(Decimal(1)/Decimal(ans)))
