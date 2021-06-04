import bisect
from itertools import accumulate
n,m = list(map(int,input().split()))
h = sorted(list(map(int,input().split())))
w = list(map(int,input().split()))
# print(h)
# print(w)
first = list(accumulate(h[::2]))
second = list(accumulate(h[1::2]))
print(first)
print(second)

arr_1 = []
arr_2 = []


ans = float("inf")
index = 0
for i in w:
    index = bisect.bisect_left(h,i)
    if(index%2 == 0 and index > 2): 
        plus = first[index//2]+(second[-1]-second[index//2-1])
        minus = second[index//2 - 2] + h[index-1] + (first[-1] - first[index//2])
    elif(index%2 == 0 and index > 2):
        plus = first[index//2]+h[index-1]+(second[-1]-second[index//2-1])
        minus = second[index//2 - 2]  + (first[-1] - first[index//2])
    elif(index%2 == 0):
        plus = first[0] + second[-1]
        minus = h[index-1] + first[-1-first[0]]
    elif(index%2 == 1):
        plus = h[index-1] + second[-1]
        minus = first[-1]
    print(plus,minus)
    ans = min(ans,abs(plus - minus))
print(ans)

    
    # print("tall",sorted(h+[i]))
    # print(tall[::2],tall[1::2],sum(tall[::2]),sum(tall[1::2]), sum(tall[::2])-sum(tall[1::2]))
    # ans = min(ans, abs(sum(tall[::2])-sum(tall[1::2])))
print(ans)
