r = [list(map(int,input().split())) for _ in range(2)]
#print(r)
pality=sum(r[0])+sum(r[1])
ans = 0
#a = r[0][0], b = r[0][1] , c= [1][0], d = [1][1]
#0手
if(r[0][0] == r[1][0] and r[0][1] == r[1][1]):
  print(ans)
  exit()
#1手
elif(r[0][0] + r[0][1] == r[1][0] + r[1][1] or r[0][0] - r[0][1] == r[1][0] - r[1][1] or (abs(r[0][0]-r[1][0])+abs(r[0][1]-r[1][1])) <= 3 ):
  ans = 1
  print(ans)
  exit()
#2手
elif(pality%2 == 0 or (abs(r[0][0]-r[1][0])+abs(r[0][1]-r[1][1])) <= 6):
  ans = 2
  print(ans)
  exit()
elif(  abs( (r[0][0] + r[0][1])-(r[1][0] + r[1][1]) ) <= 3 or  abs( (r[0][0] - r[0][1])-(r[1][0] - r[1][1]) ) <= 3    ):
  ans = 2
  print(ans)
  exit()
else: 
  ans = 3
  print(ans)
  exit()
