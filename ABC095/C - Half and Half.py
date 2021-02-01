A,B,C,X,Y = list(map(int,input().split()))
ans = 0
if(2*C < A+B):
  if(X == Y):ans = (C*X*2)
  elif(X > Y):ans = min((C*Y*2 + (X-Y)*A),(C*X*2))
  elif(X < Y):ans = min((C*X*2 + (Y-X)*B),(C*Y*2))
elif(2*C >= A+B):ans = (X*A + Y*B)
print(ans)
