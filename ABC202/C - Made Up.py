n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = [0]*n
ans = 0
cnt = [0]*(n+1)
for j in range(n):
    cnt[b[c[j]-1]-1] += 1 
# print(cnt)
for i in a:
    ans += cnt[i-1] 
 
print(ans)
