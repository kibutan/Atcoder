import sys
import math

input  = sys.stdin.readline
n = int(input())
ok = 0
ng = n + 2
def is_ok(k):
    return
total = (n*(1 + n))/2
middle = math.ceil((ng + ok)/2)
while(ng - ok > 1 ):
    if(total > n):ng = middle
    elif(total <= n):ok = middle
    middle = (ng + ok)//2
    total = (middle*(1 + middle)) /2
#     print("sum",total,"mid",middle)
# print("ans",ok)
# print("Log")
print(n - (ok - 1))
