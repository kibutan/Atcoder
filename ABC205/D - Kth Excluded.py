import bisect
# n = int(input())
n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
k = [int(input()) for i in range(q)]
 
for i in range(q):
    ans = k[i]
    index = 0
    while True:
        new_index = bisect.bisect_right(a,ans)
        if index == new_index:break
        ans += new_index - index
        index = new_index
    print(ans)
