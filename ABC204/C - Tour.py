import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# ab = [map(int,input().split()) for _ in range(m)]
ans = 0

ROUTE = {}
for i in range(m):
    a, b = map(int, input().split())
    if (a in ROUTE) == False:
        ROUTE[a] = []
    ROUTE[a].append(b)

sys.setrecursionlimit(10**5)

# from collections import defaultdict
# adj = defaultdict(set)

# ans = 0

# for a,b in ab:
#     adj[a].add(b)
# seen = [0]*(n+1)

# def dfs(pos):
#     if seen[pos]:return
#     seen[pos] = 1
#     if pos not in adj:return
#     for next_ in adj[pos]:
#         if not seen[next_]:dfs(next_)

def dfs(pos):
    if seen[pos]:return
    seen[pos] = 1
    if pos not in ROUTE:return
    for next_ in ROUTE[pos]:
        if not seen[next_]:dfs(next_)

for i in range(1,n+1):
    seen = [0]*(n+1)
    dfs(i)
    ans += sum(seen)
print(ans)
