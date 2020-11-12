N, K = list(map(int,input().split()))
l = sorted(list(map(int,input().split())),reverse = True)[:K]
print(sum(l))
