n ,m  = list(map(int,input().split()))
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))
ans = sorted(list(a.symmetric_difference(b)))
if(ans != []):print(*ans)
