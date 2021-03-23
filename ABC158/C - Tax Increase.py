def solve(a,b):
  x = (b - a)*50
#  print(x)
  if(x != 0 and int(x * 0.08) == a and int(x * 0.1) ==b):return int(x)
  elif(x == 0):
    if(a == 0):return 9
    elif(a == 1):return 13
    elif(a == 2):return 25
    elif(a == 3):return 38
    else: return -1
  else:return -1
a,b = list(map(int,input().split()))
print(solve(a,b))
