import sys

sys.setrecursionlimit(10**7)
n,q = map(int,input().split())
ab = [map(int, input().split()) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]
px = [map(int, input().split()) for i in range(q)]
p,x = [list(i) for i in zip(*px)]
ans = {}

for i in range(1,n+1):
    ans.setdefault(i,0)
ki = {}
for i in range(n-1):
    ki.setdefault(a[i],[]).append(b[i])
print(ki)
# print("ans",ans)

def add(node,point):
    if node in ki.keys():
        ans[node] += point
        # print("ki no nakamim ga aru",node)
        for i in ki[node]:
            add(i,point)
        # def add(ki no nakami,point)
    else:ans[node] += point

for j in range(q):
    add(p[j],x[j])
print(ans)
