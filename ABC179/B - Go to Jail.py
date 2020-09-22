N = int(input())
cnt = 0
flag = 0
for i in range(N):
  D = list(map(int,input().split()))
  if(D[0] == D[1]):cnt = cnt+1
  if(cnt >= 3):flag=1
  if(D[0] != D[1]):cnt = 0
if(flag == 1):print("Yes")
else:print("No")
