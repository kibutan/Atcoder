n = int(input())
h = list(map(int,input().split()))
ans = max(h)
print(h.index(ans)+1)
