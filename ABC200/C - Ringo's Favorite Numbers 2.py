n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n-1):
  for j in range(i+1,n):
    if(str(a[i])[-1] != str(a[j])[-1] or str(a[i])[-2] != str(a[j])[-2]):continue
    
    if(abs(a[i]-a[j])%200 == 0):ans+=1
print(ans)
