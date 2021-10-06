from bisect import bisect_left
from itertools import accumulate

n = int(input())
a = list(map(int,input().split()))
target = sum(a)//10
if(min(a) > target):
    print("No")
    exit()
b = list(accumulate(a+a))
# print(b)
for i in range(n):
    index = bisect_left(b,target + b[i])
    if(b[index] == target + b[i]):
        print("Yes")
        exit()
else:print("No")
    
