from decimal import *
import math
N = int(input())
x = list(map(int,input().split()))
dis_manh = 0
dis_yurc = 0
dis_chev = 0
for i in range(N):
  dis_manh = dis_manh + math.fabs(x[i])
  dis_yurc = dis_yurc + math.fabs(x[i])**2
  dis_chev = max(math.fabs(dis_chev), math.fabs(x[i]))
print("{:.15f}".format(Decimal(dis_manh)))
print("{:.15f}".format(Decimal(math.sqrt(dis_yurc))))
print("{:.15f}".format(Decimal(dis_chev)))
