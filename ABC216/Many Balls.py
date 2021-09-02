n = int(input())
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]
max = 10**18
# balls_max = 2**119
# print(max < balls_max)

ans = ""
b_max = 0
for i in range(119):
    if( 2**i < n <= 2**(i+1)):
        b_max = (i+1)
        break

for i in range(120):
    amari = 0
    if n == 0:break
    elif n == 1:ans += "A"
    else:
        amari = n % 2
        shou = n // 2
        if(amari == 1):ans += "AB"
        else:ans += "B"
    n = n // 2
print(ans[::-1])
