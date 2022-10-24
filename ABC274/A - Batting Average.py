from decimal import Decimal,ROUND_HALF_UP
a,b = map(int,input().split())
rate = Decimal(b/a)
ans = rate.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(ans)
