from decimal import Decimal
from math import sqrt


a,b = map(int,input().split())

taikakusen = Decimal(sqrt(a**2 + b**2))
# print(taikakusen)
print(Decimal(a/taikakusen) , Decimal(b/taikakusen))
