N = list(map(int,input().split()))
def digitSum(n):
  s = str(n)
  array = list(map(int,s))
  return sum(array)
total = 0
for i in range(N[0]+1):
  if(N[1] <= digitSum(i) and digitSum(i) <= N[2]):
    total += i
print(total)
