#class people():
#  x,y = None
n = int(input())
for i in range(n):
  a = int(input())
  xy = [list(map(int,input().split())) for _ in range(a)]
for i in range(2**n):
  honest = []
  for j in range(n):
    if((i >> j)&1):
      honest.append(j+1)
  print(honest)
print(xy)
