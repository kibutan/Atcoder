from decimal import Decimal
a,b = list(map(int,input().split()))
print(Decimal((a-b)*100/a))
