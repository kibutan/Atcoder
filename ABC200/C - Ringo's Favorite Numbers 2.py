n = int(input())
a = list(map(int,input().split()))
ans = 0
cnt = [0]*200
def answer(n):
  return int(n*(n+1)/2)
for i in range(n):
  cnt[a[i]%200] += 1
for j in cnt:
  ans += (j-1)*((j-1)+1)/2
#print(cnt)
print(int(ans))
