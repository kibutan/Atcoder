x = int(input())
#i^j
ans = 1
for i in range(2, x+1):
  for j in range(2,11): #上限1000 < 2^10
    if(i**j <= x and i**j > ans):ans = i**j
    else:continue
print(ans)
