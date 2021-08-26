import sys
input = sys.stdin.readline
ans = 0
n,m = map(int ,input().split())
s = [list(map(int, input().split())) for _ in range(m)]
# 無向グラフの典型入力
from collections import defaultdict
adj = defaultdict(list)
for a, b in s:
    adj[a].append(b)
    adj[b].append(a)
# print(adj)
for i,j in adj.items():
    cnt = 0
    for k in j:
        if( i > k):cnt += 1
    if(cnt == 1):ans += 1
print(ans)