N = int(input())
def digitSum(n):
  s = str(n)
  array = list(map(int,s))
  return sum(array)

ans = 100
for a in range(1,N):
  b = N - a
  ans = min(ans,(digitSum(a)+digitSum(b)))

print(ans)
