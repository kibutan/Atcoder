from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))
unique = 0
ans = 0
r = 0
# count =  for i in range(100001)]
window = defaultdict(int) #0で初期化された辞書
for l in range(n):
    while r < n:
        if window[a[r]] == 0:
            if unique == k: break
            unique += 1
        window[a[r]] += 1
        r += 1
    ans = max(ans, r - l)
    window[a[l]] -= 1
    if window[a[l]] == 0:
        unique -= 1
print(ans)
