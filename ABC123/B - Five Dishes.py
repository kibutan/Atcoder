from decimal import Decimal
import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
def add(n):
  return (n//10*10+math.ceil(Decimal(n%10)/Decimal(10))*10)
def sub(n):
  if(n%10 != 0):
    return n%10
  else:return 99
sub = (min(sub(a),sub(b),sub(c),sub(d),sub(e)))
if sub == 99:print(add(a)+add(b)+add(c)+add(d)+add(e))
else:print(add(a)+add(b)+add(c)+add(d)+add(e)-10 + sub)
