N = int(input())
p = [tuple(map(int, input().split())) for i in range(N)]
tilt = 0
for i in range(N):
  for j in range(i):
    for k in range(j):
      x1 = p[i][0] - p[k][0]
      y1 = p[i][1] - p[k][1]
      x2 = p[j][0] - p[k][0]
      y2 = p[j][1] - p[k][1]
      if(x1*y2 == x2*y1):
        print("Yes")
        exit()
else:
  print("No")
