from itertools import accumulate
from bisect import bisect_right
n = int(input())
a = list(map(int,input().split()))
a_accum = list(accumulate(a))
x = int(input())
sum_a = sum(a)
quotient = x // sum_a
reminder = x % sum_a
# print(a_accum)
index = bisect_right(a_accum,reminder)
print(quotient*len(a)+index + 1)
