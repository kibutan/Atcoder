# n = [list(map(int,input().split()))]
n,k = map(int,input().split())
# o = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        room = i*100 + j
        # print(room)
        ans += room
print(ans)
