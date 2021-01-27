#わざわざ全探索で
n = int(input())
for i in range(0,n//7+2):
  for j in range(0, n//4+2):
    if((7*i)+(4*j) == n):
      print("Yes")
      exit()
print("No")
