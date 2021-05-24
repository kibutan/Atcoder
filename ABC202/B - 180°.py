s=input()
ans = []
for i in s:
  if(i == "9"):
    ans.append("6")
  elif(i == "6"):
    ans.append("9")
  else:
    ans.append(i)
for i in range(len(ans)-1,-1,-1):
  print(ans[i],end="")
  
