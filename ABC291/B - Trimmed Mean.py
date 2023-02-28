n=int(input())
x=sorted(list(map(int,input().split())))
x_rev = x[::-1]

ans = sum(x) - sum(x[:n]) - sum(x_rev[:n])
print(ans/(3*n))
