A,B = list(map(int,input().split()))
ans = 0
if B == 1: ans = 0
else:
  ans += 1
  B -= A
  while(B > 0):
    B -= (A-1)
    ans += 1
print(ans)
