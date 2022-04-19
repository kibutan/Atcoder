xy = [list(map(int,input().split())) for i in range(3)]
for i in xy:
  x,y = list(zip(*xy))

for j in x:
  if(x.count(j) == 1):
    ans_x = j
  
for k in y:
  if(y.count(k) == 1):
  	ans_y = k

print(ans_x,ans_y)
