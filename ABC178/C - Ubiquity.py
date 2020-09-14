N = int(input())
temp = [0 for m in range(N)]
cnt = 0
for j in range(N):
  for i in range(N):
    for a in range(1,9,1):
      temp[i] = a
      if temp[i] == 0&temp[j]==9: cnt = cnt + 1
print(cnt)
