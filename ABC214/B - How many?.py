# n = int(input())
s,t = list(map(int,input().split()))
cnt =0
# m = [list(map(int,input().split())) for i in range(n)]
for a in range(s+1):
    for b in range(s+1):
        for c in range(s+1):
            if(a + b + c <= s and a*b*c  <= t):cnt += 1
print(cnt)
