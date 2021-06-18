n,m = map(int,input().split())
ab = [map(int,input().split()) for _ in range(m)]
import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict
adj = defaultdict(set)
ans = 0
seen = [False]*(n+1)
for a,b in ab:
    adj[a].add(b)
    adj[b].add(a)
# print(adj)
cnt = 0

def dfs(pos):
    seen[pos] = True
    for next_ in adj[pos]:
        if not seen[next_]:
            dfs(next_)

for i in range(1,n+1):
    if not seen[i]:
        dfs(i)
        cnt += 1
print(cnt-1)
