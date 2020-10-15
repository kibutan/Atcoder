N = int(input())
flag = 0
for i in range(9):
  for j in range(9):
    if(N == (i + 1)*(j + 1)):
      flag = 1
      break
if(flag == 1):print("Yes")
else:print("No")
    
