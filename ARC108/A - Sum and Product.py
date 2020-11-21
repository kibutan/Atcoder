S,P  = list(map(int,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#print(make_divisors(S))
div = make_divisors(P)
for i in div:
  for j in div:
#    print("i"+str(i))
#    print("j"+str(j))
    if(i+j == S):
#      print(S)
      print("Yes")
      exit()
print("No")
    
    
