import math
def combinations(n,r):
  return math.factorial(n) // (math.factorial(n-r)*math.factorial(r))
n,m = list(map(int,input().split()))
cnt = 0
if(n <= 1 and m <= 1):print(0)
elif(n <= 1):print(combinations(m,2))
elif(m <= 1):print(combinations(n,2))
else:print(combinations(n,2) + combinations(m,2))
