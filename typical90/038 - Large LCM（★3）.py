from math import gcd
from decimal import Decimal
a,b = list(map(int,input().split()))
ans = Decimal(a*b)/Decimal(gcd(a,b))
if ans > 10**18:print("Large")
else:print(ans)
