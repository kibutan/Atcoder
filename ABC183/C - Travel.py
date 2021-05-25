import itertools
N,K =list(map(int, input().split()))
a = [[0,0,0,0]] + [list(map(int,input().split())) for l in range(N)]
print(a)
path = [0]*N
cnt = 0
for i in range(1,N+1):
  ans = 0
  path = [(0,0,0)] + list(itertools.permutations(range(2,N+1),N-1))
#  ans += a[i-1][path[i-1][0]]
#  ans += a[N][path[N][0]]
  for j in range(1,N):
    ans += a[j][path[j][0]-1]
    print("tekitou",a[j][path[j][0]-1])
  
print(path)

