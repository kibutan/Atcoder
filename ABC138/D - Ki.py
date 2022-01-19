import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,q = map(int,input().split())
ki= {}
for i in range(n-1):
    a,b = map(int,input().split())
    ki.setdefault(a,[]).append(b)
    ki.setdefault(b,[]).append(a)
cost = {x: 0 for x in range(1,n+1)}
for i in range(q):
    p,x = map(int,input().split())
    cost[p] += x
ans = {x: 0 for x in range(1,n+1)}
arrived = {x: 0 for x in range(1,n+1)}
for i in range(1,n+1):
    ans.setdefault(i,0)
def calc_cost(node,parent_cost=0):
    arrived[node] = True
    parent_cost += cost[node]
    ans[node] = parent_cost
    for i in ki[node]:
        if not arrived[i]:
            calc_cost(i,parent_cost)
        else:continue
calc_cost(1)
print(*ans.values())
