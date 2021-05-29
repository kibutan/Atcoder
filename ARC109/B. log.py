import sys
from decimal import Decimal

input  = sys.stdin.readline
n = int(input())
ok = 0
ng = 10**20
# print(ok,ng)
def is_ok(k):
    return

# n+1を切り出して1,2,...,xまで切り出せるときのxの値を知りたい。
while(ng - ok > 1 ):
    middle = (ng + ok)//2
    total = (middle*(1 + middle))//2
    if(total > (n+1)):ng = middle
    elif(total <= (n+1)):ok = middle

#     print("sum",total,"mid",middle)
# print("ans",ok)
# print("Log")
print(n-(ok-1))
