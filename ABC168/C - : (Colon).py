from decimal import Decimal
import math
A,B,H,M = list(map(Decimal,input().split()))
Deg_M = Decimal(0 if M == 0 or M == 60 else Decimal(360)*Decimal(M/60))
Deg_H = Decimal(0 if H == 0 or H == 12 else Decimal((Decimal(360)*Decimal(H/12) + Decimal(360/12)*Decimal(M/60))))

theta = 0

if(abs(Deg_H - Deg_M) == 0):print(abs(A-B))
elif(abs(Deg_H - Deg_M) == 180):print(A+B)
else:
  theta = Decimal(abs(Deg_H - Deg_M))
#  print(Deg_H)
#  print(Deg_M)
#  print(Decimal(round(math.cos(Decimal(Decimal(math.radians(theta)))),15)))
  cos = Decimal(round(math.cos(Decimal(Decimal(math.radians(theta)))),15))
  power = Decimal((Decimal(A*A)+Decimal(B*B))-2*Decimal(A)*Decimal(B)*cos)
  print(math.sqrt(power))
