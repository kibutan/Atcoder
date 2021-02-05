n = int(input())
p = list(map(int,input().split()))
p_sorted = sorted(p)
cnt = 0
for i in range(n):
  if( p[i] != p_sorted[i]):cnt+=1
  else:continue
if(cnt <= 2 and cnt !=1):print("YES")
else:print("NO")
