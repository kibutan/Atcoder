n = int(input())
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]
if n <= 125:print(4)
elif 126 <= n <= 211:print(6)
else:print(8)
