m = list(map(int,input().split()))
if(0 in m and 1 in m):print(2)
elif(2 in m and 1 in m):print(0)
elif(2 in m and 0 in m):print(1)
else:print(m[0])
