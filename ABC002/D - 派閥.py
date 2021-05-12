from itertools import combinations
ans = 0
n,m= list(map(int,input().split()))
xy = [tuple(map(int,input().split())) for _ in range(m)]
xy_set = xy
arr = []
flag = 1
#print(xy_set)
for i in range(2 ** n):
    arr = []
    for j in range(n):
        if((i >> j) & 1):
            arr.append(j+1)
    # print("arr:",arr)
    for v in combinations(arr,2):
        flag = 1
        # print("combinations",v)
        # print("xy_set",xy_set)
        # print("nCr in xy_set",v in xy_set)
        if not(v in xy_set):
            flag = 0
            break
    if (flag == 1):
        ans = max(ans,len(arr))
        # print()
        # print("Passed!",len(arr))
        # print()
print(ans)
    
