n = int(input())
w = [input() for _ in range(n)]
ans = "Yes"
if(len(w) != len(set(w))):
  print("No")
  exit()
else:
  for i in range(n-1):
    if(w[i][-1] == w[i+1][0]):continue
    else:
      print("No")
      exit()
print("Yes")
