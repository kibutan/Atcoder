import sys
input = sys.stdin.readline
import bisect
 
n = int(input())
a = sorted(list(map(int,input().split())))
q = int(input())
for i in range(q):
    r = int(input())
    # print(bisect.bisect_left(a,i))
    idx = bisect.bisect_left(a,r)
    ans = float("inf")
    if idx < n:
        ans = min(ans,abs(a[idx] - r))
    if idx > 0:
        ans = min(ans,abs(a[idx - 1] - r))
    print(ans)
