from decimal import Decimal
from typing import AnyStr
# n = int(input())
a,b,c,d = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]
if(b/c >= d):print(-1)
else:
    for i in range(1,10**5+1):
        score = (a+(b*i))/(c*i)
        if score <= d:
            print(i)
            exit()
