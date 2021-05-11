n,m= list(map(int,input().split()))
xy = [list(map(int,input().split()))]
arr = []
for i in range(2 ** n):
    arr = []
    for j in range(n):
        if((i >> j) & 1):
            arr.append(j)
    print(arr)
