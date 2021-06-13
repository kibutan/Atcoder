import math
# n = int(input())
a,b,c = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

if a == 0 and b == 0:print("=")
elif a == 0 and b > 0:print("<")
elif a == 0 and b < 0:
    if c%2 == 0:
        print("<")
    else:
        print(">")
elif b == 0 and a > 0:print(">")
elif b == 0 and a < 0:
    if c%2 == 0:
        print(">")
    else:
        print("<")
elif a > 0 and b > 0:
    if a > b: print(">")
    elif a < b: print("<")
    elif a == b: print("=")
elif a < 0 and b > 0:
    if c%2 == 0:
        if abs(a) == abs(b):print("=")
        elif abs(a) > abs(b):print(">")
        elif abs(a) < abs(b):print("<")
    else:
        print("<")
elif a > 0 and b < 0:
    if c%2 == 0:
        if abs(a) == abs(b):print("=")
        elif abs(a) > abs(b):print(">")
        elif abs(a) < abs(b):print("<")
    else:
        print(">")
if a < 0 and b < 0:
    if c % 2 == 0:
        if abs(a) > abs(b):print(">")
        elif abs(a) < abs(b):print("<")
        elif abs(a) == abs(b):print("=")
    else:
        if abs(a) > abs(b):print("<")
        elif abs(a) < abs(b):print(">")
        elif abs(a) == abs(b):print("=")
        
