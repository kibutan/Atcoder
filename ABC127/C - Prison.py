n,m = list(map(int,input().split()))
lr = [list(map(int,input().split())) for _ in range(m)]
l,r = [list(i) for i in zip(*lr)]
if(max(l) > min(r)):print(0)
else:print(min(r) - max(l) + 1)
