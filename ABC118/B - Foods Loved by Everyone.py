n,m = list(map(int,input().split()))
ka = [list(map(int,input().split())) for _ in range(n)]
k = []
a = []
for i in range(n):
  k.append(ka[i][0])
  a.append(ka[i][1:])
#print(k,a)
s = set(a[0])

for j in range(1,n):
  s = s&set(a[j])
#  print(s)

print(len(s))
