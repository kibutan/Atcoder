import sys

sys.setrecursionlimit(10**7)
n,q = map(int,input().split())
ab = [map(int, input().split()) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]
px = [map(int, input().split()) for i in range(q)]
p,x = [list(i) for i in zip(*px)]

cost = {x: 0 for x in range(1,n+1)}
ans = {x: 0 for x in range(1,n+1)}
arrived = {x: 0 for x in range(1,n+1)}

for i in range(1,n+1):
    ans.setdefault(i,0)
ki = {}
for i in range(n-1):
    #双方向グラフを作る
    ki.setdefault(a[i],[]).append(b[i])
    ki.setdefault(b[i],[]).append(a[i])
# print(ki)

# arrived.setdefault(a[i],-1)

# print("ans",ans,"arrive",arrived)
# 両方向に辺をつないで、頂点から準にポイントを割り振り
def calc_cost(node,parent_cost=0):
    arrived[node] = True
    #親からのコストに自分のコストを乗せる、それが自分のコスト合計
    parent_cost += cost[node]
    ans[node] = parent_cost
    for i in ki[node]:
        #もし、子供がいれば、子供に自分のコストを引き継ぐ。
        if not arrived[i]:
            # print("iiiiiiiiiii",i)
            calc_cost(i,parent_cost)
        else:continue

# imosの木版。各ノードのプラス成分を登録
for i in range(q):
    cost[p[i]] += x[i]
# print("Hogehoge",ans)

# 入力は木 = すべてつながっているので呼び出しは一回でいい。
calc_cost(1)
# print("ans",*ans.values())
print(*ans.values())
