import collections
n = int(input())
ab = [list(map(int,input().split())) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]
a += b
c_a = collections.Counter(a).most_common()[0]

if(c_a[1] == n-1):
    print("Yes")
    exit()
print("No")
