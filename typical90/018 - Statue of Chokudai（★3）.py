import math
from decimal import Decimal
t = int(input())
l,x,y = list(map(int,input().split()))
q = int(input())
e = [int(input()) for _ in range(q)]

for i in range(q):
    # print((e[i]/t))
    # print("pi*",Decimal(math.cos(Decimal(math.pi)*((Decimal(3/4)-Decimal((e[i]/t)))*2))))
    # print(0,math.cos(Decimal(math.pi)*((Decimal(3/4)-Decimal(e[i]/t))*2)),math.sin(Decimal(math.pi)*((Decimal(3/4)-Decimal(e[i]/t))*2))+1)
    e_y = Decimal(l/2)*Decimal(math.cos(Decimal(math.pi)*((Decimal(3/4)-Decimal(e[i]/t))*2)))
    e_z = Decimal(l/2)*Decimal((math.sin(Decimal(math.pi)*((Decimal(3/4)-Decimal(e[i]/t))*2))+1))

    diff_xy = math.sqrt(x**2+(e_y-y)**2)
    # print("ans+++++++++++++",math.degrees(Decimal(math.atan2(e_z,diff_xy))))
    print(math.degrees(Decimal(math.atan2(e_z,diff_xy))))
