N = list(map(int,input().split()))
print(min(N[0]%N[1],N[1]-(N[0]%N[1])))
