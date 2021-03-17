import heapq
import math
def discount(x):
  x *= -1
  x = x // 2
  return -1*x
n,m = list(map(int,input().split()))
a = list(map(lambda x :int(x)*(-1),input().split()))
heapq.heapify(a)
for i in range(m):
  heapq.heappush(a,discount(heapq.heappop(a)))
#  print(a)
print(sum(a)*-1)
