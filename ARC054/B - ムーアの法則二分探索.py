import sys
from decimal import Decimal
import math
input = sys.stdin.readline
p = Decimal(input())

def f(x): #求める方程式
    return Decimal(x) + Decimal(p/pow(2,(Decimal(x)/Decimal(1.5))))

def fd(x): #1回微分
    return Decimal(1)+(Decimal(p*Decimal(math.log(pow(2,(Decimal(-1/1.5))))))*Decimal(pow(2,Decimal(Decimal(-x)/Decimal(1.5)))))


ok = p
ng = 0
cnt = 1000
while cnt > 0:
    cnt -= 1
    middle = (ok+ng)/2
    if(fd(middle) == 0):
        break
    elif(fd(middle) < 0):
        ng = middle
        continue
    elif(fd(middle) >0):
        ok = middle
        continue
print(f(middle))
