from collections import defaultdict
n,q = list(map(int,input().split()))
pab = [list(map(int,input().split())) for _ in range(q)]
p,a,b = [list(i) for i in zip(*pab)]
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
 
uf = UnionFind(n)
for i in range(q):
    if p[i] == 0:uf.union(a[i],b[i])
    else:print("Yes") if uf.same(a[i],b[i]) else print("No")
