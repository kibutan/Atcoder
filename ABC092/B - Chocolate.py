n = int(input())
d ,x = list(map(int,input().split()))
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
  ans += 1 + (d-1)//a[i]
print(ans+x)
