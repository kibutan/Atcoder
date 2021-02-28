import math
def Eratosthenes(n):
  a=list(range(2,n+1))
  p=[]
  while a[0]**2 <=n:
    tmp=a[0]
    p.append(tmp)
    a = [e for e in a if e%tmp!=0]
  return p+a
 
def factrization(n):
  factor = {}
  for i in Eratosthenes(n):
    div_cnt = 0
    while n%i == 0:
      div_cnt += 1
      n //= i
    if div_cnt != 0:
      factor[i] = div_cnt
  return factor


cnt = 0
n = int(input())
#print(Eratosthenes(n))
for i in Eratosthenes(n):
  j = 2
#  print(i)
#  print(math.pow(n,1/i))
  while(i ** j <= n):
    print(i,j,i**j)
    cnt += 1
    j += 1
  j = 2
print(n - cnt)
