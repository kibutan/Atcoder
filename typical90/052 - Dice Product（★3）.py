from decimal import Decimal
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
div = 10**9+7

ans = 1
for i in a:
    hole = 0
    hole += sum(i)
    ans *= hole
    ans %= div
print(ans)
