from itertools import combinations
import collections
n = int(input())
a = sorted(list(map(int,input().split())))

ans = (n*(n-1))//2
a_keys = range(n)
a_set = set(a)
a_cnt = collections.Counter(a)
cnt =0
# print(a_cnt)
for i in a_cnt.values():
    ans -= (i*(i-1))//2
print(ans)
