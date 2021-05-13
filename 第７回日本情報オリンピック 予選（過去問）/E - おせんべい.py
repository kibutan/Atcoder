r,c = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(r)]
ans = 0
for i in range(2**r):
    arr = []
#  print(i)
    for j in range(r):
        if((i >> j)&1):
            arr.append(j)
    print(arr)
    for k in range(r):
        if k in arr:
            print("1st:",list(map(lambda x:(x+1)%2,a[k])))
            a[k] = list(map(lambda x:(x+1)%2,a[k]))
        else:
            print(a[k])
    for i in range(c):
        cnt = 0
        for j in range(r):
            # print((a[j][i]+1)%2,end = "")
            if(a[j][i] == 0):cnt+=1
        if(cnt >= r//2):(a[j][i]+1)%2
        print(a[j])
