import sys
from decimal import Decimal
import math
input = sys.stdin.readline
p = Decimal(input())
x = Decimal(1.5) * Decimal(math.log2(Decimal(2/3)*p*Decimal(math.log(2))))
if(x >= 0):
    ans = x + p/Decimal(pow(2,Decimal(2/3)*x))
else:
    ans = p
print(ans)
