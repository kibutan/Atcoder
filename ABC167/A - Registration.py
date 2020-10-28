T = input()
S = input()
ans = "No"
if(len(T)+1 == len(S)):
  for i in range(len(T)):
    if(T == S[0:len(T)]):ans = "Yes"
    else:break
print(ans)
