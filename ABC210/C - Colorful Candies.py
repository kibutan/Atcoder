from collections import Counter
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
c= list(map(int,input().split()))

cnt = Counter(c[:k])
ans = len(cnt)

# print(cnt)
for i in range(0,n-k):
    cnt.update([c[k+i]])
    if(cnt[c[i]] == 1):del cnt[c[i]]
    else:cnt.subtract([c[i]])
    ans = max(ans,len(cnt))
    # print(cnt)
    # print(len(cnt))
print(ans)
