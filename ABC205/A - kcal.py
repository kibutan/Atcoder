from decimal import Decimal
# n = int(input())
a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

print(Decimal(a * b /100))
