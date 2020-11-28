a,b,x,y = list(map(int,input().split()))
ans = 0
if(a == b):ans = x
elif(a < b):
  if(2*x < y):ans = (1+2*(b-a))*x
  else:ans = (b-a)*y+x
else:
  if(2*x < y):ans = (2*(a-b)-1)*x
  else:ans = (a-b-1)*y+x
print(ans)
