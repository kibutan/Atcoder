from collections import deque
n  = int(input())
ab = [map(int,input().split()) for _ in range(n-1)]
 
max_dist = 0
max_pos = 0
 
import sys
sys.setrecursionlimit(10 ** 9)
 
from collections import defaultdict
adj = defaultdict(set)
for a,b in ab:
    adj[a-1].add(b-1)
    adj[b-1].add(a-1)
    #通路を双方向で結んでいる? 都市1を0としているように見える
# print(adj)
 
def dfs(pos,seen,dist):
    seen[pos] = True
 
    global max_dist,max_pos
    if max_dist < dist:
        max_dist = dist
        max_pos = pos
    for next_ in adj[pos]:
        if not seen[next_]:
            dfs(next_,seen,dist + 1)
 
dfs(0,[False]*n,0)
dfs(max_pos,[False]*n,0)
 
print(max_dist+1)
