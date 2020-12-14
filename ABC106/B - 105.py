def make_divisors(n):
  lower_divisors, upper_divisors = [],[]
  i = 1
  while i * i <=n:
    if(n % i == 0):
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

n = int(input())
ans = 0
for j in range(1,n+1,2):
  if(len(make_divisors(j)) == 8):
    ans+=1
#    print(j)
print(ans)
