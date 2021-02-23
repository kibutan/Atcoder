n,m,c = list(map(int,input().split()))
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(n)]
score = 0
ans = 0
for j in range(n):
  score = 0
  for i in range(m):
    score += a[j][i] * b[i]
#    print("a[j][i] * b[i]",a[j][i] * b[i])
#    print("a[j][i]",a[j][i])
#    print("b[i]",b[i])

#  print("score",score + c)
  if(score + c > 0 ):ans+=1
print(ans)
