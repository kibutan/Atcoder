import bisect
N = int(input())
A = list(map(int,input().split()))
A.sort()
B = list(map(int,input().split()))
C = list(map(int,input().split()))
C.sort()
ans = 0
ab = 0
bc = 0
for i in range(N):
    bc = (bisect.bisect_right(C,B[i]))
    ab = (bisect.bisect_left(A,B[i]))
    ans += ab*(len(C) - bc)
print(ans)
