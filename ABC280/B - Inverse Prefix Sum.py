n = int(input())
s = list(map(int,input().split()))
if n == 1:
  print(s[0])
  exit()
print(s[0],end = " ")
for i in range(1,n-1):
  print(s[i]-s[i-1], end = " ")
print(s[-1]-s[-2])
