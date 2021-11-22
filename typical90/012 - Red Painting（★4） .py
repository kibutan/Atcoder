from collections import defaultdict

h,w = list(map(int,input().split()))
Q = int(input())
q = [list(map(int,input().split())) for _ in range(Q)]
color = [[0 for i in range(w)]for j in range(h)]
# print(color)
#(0,0)の形で管理したい
# https://note.nkmk.me/python-union-find/#:~:text=keys%2C%20values%2C%20items%EF%BC%89-,%E6%96%87%E5%AD%97%E5%88%97%E3%82%84%E3%82%BF%E3%83%97%E3%83%AB%E3%81%AA%E3%81%A9%E3%82%92%E8%A6%81%E7%B4%A0%E3%81%A8%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88,-%E4%B8%8A%E3%81%AE%E4%BE%8B%E3%81%AE
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) #つなぎ直しの工夫
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y :
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self, x,y):
        return self.find(x) == self.find(y) 

class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))
        
        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x],self.d[y])

    def same(self, x, y):
        return super().same(self.d[x],self.d[y])

label = []
for i in range(h):
    for j in range(w):
        label.append((i,j))

# print(label)

ufl = UnionFindLabel(label)
# print("--Typ90----")

for i in range(Q):
    if q[i][0] == 1:
        # 上下左右の時のみUnionをどう実現する?
        # print(ufl.members())
        # https://wakame.tech/posts/20210818_typical_90
        # https://atcoder.jp/contests/typical90/submissions/24758502
        # とりあえず該当の座標に色を塗るcolor[x][y] = 1
        color[q[i][1] -1][q[i][2]-1] = 1
        # 塗った箇所の4方をチェックしcolor = 1の箇所が有ればUnionする。
        # 塗るたびに4方を確認させることですでに周りが赤い時も正しくUnionできそう。
        for k in [(0,-1),(-1,0),(0,1),(1,0)]:
            # 塗った隣が枠からはみ出るとき(q[i][1]-1 + k[0] >wとか)はContinueする
            if (q[i][1]-1 + k[0] >= h or q[i][1]-1 + k[0] < 0
                or q[i][2] - 1 + k[1] >= w or q[i][2]-1 + k[1] < 0):continue
            # 塗った隣がcolor = 1の時、Unionする
            if color[ (q[i][1] -1) + k[0] ][q[i][2]-1 + k[1] ] == 1:
                ufl.union(((q[i][1] -1) + k[0], q[i][2]-1 + k[1] ),(q[i][1] -1 , q[i][2] -1))
    else:
        if ufl.same((q[i][1]-1,q[i][2]-1),(q[i][3]-1,q[i][4]-1)) and color[q[i][1] -1][q[i][2] -1] == 1 and color[q[i][3] -1][q[i][4] -1] == 1:
            print("Yes")
        else:print("No")
