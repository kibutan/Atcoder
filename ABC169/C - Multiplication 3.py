from decimal import Decimal
A = list(map(Decimal,input().split()))
mul = 1
for i in A:
  mul *= i
print(int(mul))
