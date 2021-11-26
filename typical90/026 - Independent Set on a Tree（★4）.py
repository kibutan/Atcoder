import sys
sys.setrecursionlimit(10**6)

def coloring(pos,cur_col):
    global arrive
    global n
    if(arrive[pos]):return
    arrive[pos] = True
    color[pos] = cur_col
    for i in G[pos]:
        if color[i] == -1:
            coloring(i,1-cur_col)


n = int(input())
G= dict()
for i in range(1,n+1):
    G[i] = set()

for _ in range(n-1):
    a,b = [int(x) for x in input().split()]
    G[b].add(a)
    G[a].add(b)
# print(G)

arrive=[False for _ in range(n+1)]
color =[-1 for _ in range(n+1)]


# print(arrive)

# for i in range(n):
coloring(1,0)
# print("No")
# print("color",color)
ans = [i for i , x in enumerate(color) if x == 0] if color.count(0) >= (n//2) else [i for i , x in enumerate(color) if x == 1]
print(*ans[:n//2])
