t = int(input())
for i in range(t):
  cnt = 0
  n = int(input())
  a = list(map(int,input().split()))
  for j in a:
    if j%2 !=0:cnt+=1
  print(cnt)
