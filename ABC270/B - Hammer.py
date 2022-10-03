def mysign(x):
  return (x > 0) - (x < 0)

def calc_cost(x,z):
  if(mysign(x) == mysign(z)):return abs(x)
  else:return abs(x) + abs(2*z)
  
x,y,z = map(int,input().split())
if(mysign(y) == -1):
  x = -x
  y = -y
  z = -z
if(x < y):print(abs(x))
else:
  if(z > y):print(-1)
  else:print(abs(z) + abs(x-z))
  
