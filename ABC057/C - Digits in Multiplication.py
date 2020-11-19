import math
ans = 11
N = int(input())
upper_divisors = []
#divisors = []
i = 1
while i*i <= N:
  if N % i == 0:
    upper_divisors.append(N//i)
  i += 1
  
for j in upper_divisors:
  ans = min(ans,len(str(j)))
#  print(len(str(j)))
#print("ans:"+str(ans))
#for i in range(int(sqrt(N))):
print(ans)
