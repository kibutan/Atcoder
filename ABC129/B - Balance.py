n = int(input())
w = list(map(int,input().split()))
r = 0
l = 0
#print(sum(w))
ans = 100
for i in range(n):
#  print("L-one",w[i])
#  print("L",sum(w[0:i+1]))
#  print("R",sum(w[i+1:n]))
  ans = min(ans, abs(sum(w[0:i+1])-sum(w[i+1:n])))
print(ans)
