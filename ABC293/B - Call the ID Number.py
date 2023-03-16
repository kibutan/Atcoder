from collections import deque
n = int(input())
a = list(map(int,input().split()))
skip = set()
# print(a)
for i in range(n):
    # print("call",i+1,"to",a[i])
    if (i+1) in skip:
      #  print("skipped!")
       continue
    else:skip.add(a[i])
    # print("skip", skip)
ans = set(list(range(1,n+1)))^skip
print(len(ans))
print(*sorted(list(ans)))
