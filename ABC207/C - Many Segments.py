N = int(input())
r = [0]*N
l = [0]*N

for i in range(N):
    t,l[i],r[i] = map(int,input().split())
    if t == 2:r[i] -= 0.5
    elif t == 3:l[i] += 0.5
    if t == 4:
        l[i] += 0.5
        r[i] -= 0.5
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        if max(l[i],l[j]) <= min(r[i],r[j]):cnt += 1
print(cnt)
