N = int(input())
L = sorted(list(map(int,input().split())))
cnt = 0
for i in range(N):
  for j in range(i):
    for k in range(j):
      if(L[i] != L[k] and L[i] != L[j] and L[k] != L[j] and L[i] < (L[k]+L[j])): 
        cnt = cnt +1
print(cnt)
