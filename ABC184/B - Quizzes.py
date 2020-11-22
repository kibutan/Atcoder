N,X = list(map(int,input().split()))
S = input()
 
for i in range(N):
  if(X == 0):
    if(S[i] == "x"):
      continue
    else:X += 1
  else:
    if(S[i] == "x"):X -= 1
    else:X += 1
print(X)
      
