import collections
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

mylist =[0] 
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  mylist.extend(make_divisors(A[i]))
  mylist = [i for i in mylist if i > 1]
#  print(collections.Counter(mylist))
print(collections.Counter(mylist).most_common()[0][0])
