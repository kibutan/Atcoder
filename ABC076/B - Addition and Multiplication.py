n = int(input())
k = int(input())
ans = 1

for i in range(n):
  if(ans < k):ans *= 2
  else:ans += k
print(ans)
