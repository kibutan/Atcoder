from itertools import accumulate
import bisect

n,m,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_acc = [0] + list(accumulate(a))
b_acc = list(accumulate(b))
# print(a_acc)
# print(b_acc)
ans = 0
a_limit = bisect.bisect_right(a_acc,k)
# print("a_limit",a_limit)
for i in range(a_limit):
    b_limit = bisect.bisect_right(b_acc,k-a_acc[i])
    # print("a",i,"b_limit",b_limit)
    ans = max(ans,i+b_limit)
print(ans)
