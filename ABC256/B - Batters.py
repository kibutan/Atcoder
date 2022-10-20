from itertools import accumulate


n = int(input())
a = list(map(int,input().split()))
ans = 0
accum = accumulate(a[::-1])

for i in accum:
    if i >=4 :ans += 1

print(ans)
