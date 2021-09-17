import math
from decimal import Decimal
n = Decimal(input())
for i in range(1,61):
  if n < 2**i:
    print(i-1)
    exit()
