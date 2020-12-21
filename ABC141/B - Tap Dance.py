S = input()
ans = "Yes"
for i in range(len(S)):
  if( i%2 == 0 and (S[i] == "R" or S[i] == "U" or S[i] == "D")):
    continue
  elif( i%2 == 1 and (S[i] == "L" or S[i] == "U" or S[i] == "D")):
    continue
  else:
    ans = "No"
    break
print(ans)
