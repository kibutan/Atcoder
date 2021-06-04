import bisect
n,m = list(map(int,input().split()))
h = sorted(list(map(int,input().split())))
w = list(map(int,input().split()))
# print(h)
# print(w)
ans = float("inf")
for i in w:
    tall = []
    bisect.bisect_left(h,i)
    tall = sorted(h+[i])
    # print("tall",sorted(h+[i]))
    # print(tall[::2],tall[1::2],sum(tall[::2]),sum(tall[1::2]), sum(tall[::2])-sum(tall[1::2]))
    ans = min(ans, abs(sum(tall[::2])-sum(tall[1::2])))
print(ans)
