a,k = list(map(int,input().split()))
ans = 0
while(a < 2000000000000):
  if(k == 0):
    ans = 2000000000000 - a
    break
  a += (1 + k*a)
  ans += 1
#  print(a)
print(ans)
