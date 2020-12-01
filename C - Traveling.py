N = int(input())
crd = (0,0,0)
ans = "No"

for _ in range(N):
  t,x,y = map(int,input().split())
#  print(crd)
  if(t-crd[0] < abs(x-crd[1]) + abs(y-crd[2])):
    ans = "No"
    break
  else:
    crd = (t,x,y)
    if(t % 2 != (x+y)%2 ):
      ans = "No"
      break
    else: ans = "Yes"
print(ans)
