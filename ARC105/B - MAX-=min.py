import math
from functools import reduce
def gcd(*numbers):
  return reduce(math.gcd, numbers)
N = int(input())
A = list(map(int,input().split()))
print(gcd(*A))
